from fastapi import FastAPI, APIrouter
import pdfplumber
import requests


data = APIrouter()


@data.get("/download_file/{url}")
def download_data(url):

