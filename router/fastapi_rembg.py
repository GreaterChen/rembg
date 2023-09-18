from PIL import Image
import uvicorn
from fastapi import FastAPI
import io

from pydantic import BaseModel
from starlette.responses import StreamingResponse

from utils import remove_background_img, get_img_data, pil2np

app = FastAPI()


class FileAccept(BaseModel):
    img: str
    size: int


@app.post("/upload")
async def remove_background(file: FileAccept):
    contents = get_img_data(file.img)

    img = pil2np(contents)

    user_data = {'origin_img': img, 'input_img': img, 'tmp_img': img, 'output_img': img}
    removed_img = remove_background_img(file.size, user_data)

    removed_img = Image.fromarray(removed_img)
    removed_img.show()
    byte_io = io.BytesIO()
    removed_img.save(byte_io, format="png")
    byte_io.seek(0)
    return StreamingResponse(byte_io, media_type="image/png")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
