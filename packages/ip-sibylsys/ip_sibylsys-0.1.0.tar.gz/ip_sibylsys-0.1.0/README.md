# IP-Sibyl-Core
Main functions of Sibyl-System-For-IDOLY-PRIDE

## Installation
```
python3 -m pip install ip_sibylsys
```

## General function
```
from from ip_sibylsys.match import *
```
### Convert image to binary
```
to_binary(img: cv2.typing.MatLike, thresh: float) -> cv2.typing.MatLike
```
### Convert image to binary with adaptive threshold
```
to_binary_adaptive(img: cv2.typing.MatLike, blocksize: int, C: float) -> cv2.typing.MatLike
```
### Draw text list(binary, mask), set `_half_split_length` to cut text
```
draw_text(
    text: str, font_path: list[str], font_size: list[int], stroke_width: int, kerning: int
) -> tuple[list[cv2.typing.MatLike], list[cv2.typing.MatLike]]
```
### Compare text in image to drawn text
```
compare(
    frame_img: cv2.typing.MatLike,
    binary: list[cv2.typing.MatLike],
    threshold: float,
    mask: list[cv2.typing.MatLike],
) -> bool
```
