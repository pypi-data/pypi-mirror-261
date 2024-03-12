import asyncio
import json
import os
import sys

import aiofiles
import fire
from aiobaseclient import BaseClient
from aiokit import MultipleAsyncExecution
from izihawa_netlib import ClientPool
from izihawa_textparser import DocumentChunker, GrobidParser
from izihawa_utils.file import yield_files


import copy

import langchain
from langchain.text_splitter import HeaderType
from langchain_core.documents import Document


class RecursiveCharacterTextSplitter(
    langchain.text_splitter.RecursiveCharacterTextSplitter
):
    def create_documents(
        self, texts: list[str], metadatas: list[dict] | None = None
    ) -> list[Document]:
        """Create documents from a list of texts."""
        _metadatas = metadatas or [{}] * len(texts)
        documents = []
        for i, text in enumerate(texts):
            index = -1
            for chunk in self.split_text(text):
                metadata = copy.deepcopy(_metadatas[i])
                start_index = metadata["start_index"]
                index = text.find(chunk, index + 1)
                metadata["start_index"] = start_index + index
                new_doc = Document(page_content=chunk, metadata=metadata)
                documents.append(new_doc)
        return documents



async def process_with_grobid(sciparse, filepath, target_dir):
    async with aiofiles.open(filepath, "rb") as f:
        processed_document = await sciparse.parse_paper(await f.read())
        target_filepath = os.path.join(
            target_dir, os.path.basename(filepath).removesuffix(".pdf") + ".txt"
        )
        async with aiofiles.open(
            target_filepath,
            "w",
        ) as output:
            r = await asyncio.get_running_loop().run_in_executor(
                None, lambda: json.dumps(processed_document)
            )
            print("writing", target_filepath)
            await output.write(r)


async def process_with_nougat(nougat_client, filepath, target_dir):
    async with aiofiles.open(filepath, "rb") as f:
        nougat_response = await nougat_client.post(
            data={"file": await f.read(), "type": "application/pdf"}
        )
        target_filepath = os.path.join(
            target_dir, os.path.basename(filepath).removesuffix(".pdf") + ".txt"
        )
        async with aiofiles.open(
            target_filepath,
            "w",
        ) as output:
            print("writing", target_filepath)
            await output.write(nougat_response)


async def grobid(
    source_dir: str,
    target_dir: str,
    base_url: str = "http://127.0.0.1:8070",
    threads: int = 32,
):
    executor = MultipleAsyncExecution(threads)

    grobid_client_1 = BaseClient(base_url)
    await grobid_client_1.start()

    client_pool = ClientPool([(grobid_client_1, threads)])
    sciparse = GrobidParser(client_pool)

    for filepath in yield_files(f'{source_dir.rstrip("/")}'):
        await executor.execute(process_with_grobid(sciparse, filepath, target_dir))

    await executor.join()


async def nougat(
    source_dir: str,
    target_dir: str,
    endpoint: str = "http://localhost:8503/",
    threads: int = 2,
):
    executor = MultipleAsyncExecution(threads)

    nougat_client = BaseClient(
        endpoint,
        default_headers={
            "Accept": "application/json",
        },
    )
    await nougat_client.start()

    for filepath in yield_files(f'{source_dir.rstrip("/")}'):
        await executor.execute(process_with_nougat(nougat_client, filepath, target_dir))

    await executor.join()


async def split():
    md = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "h1"),
            ("##", "h2"),
            ("###", "h3"),
            ("####", "h4"),
            ("#####", "h5"),
            ("######", "h6"),
        ],
        return_each_line=False,
    )
    for s in md.split_text(sys.stdin.read()):
        print(s)


if __name__ == '__main__':
    fire.Fire(
        {
            "grobid": grobid,
            "nougat": nougat,
            "split": split
        }
    )
