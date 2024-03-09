# WDS-AssBuilder-Core
Main functions of World-Dai-Star-ASS-Builder
## Installation
```
python3 -m pip install wds_assbuilder
```

## General function
```
from from wds_assbuilder.match import *
from from wds_assbuilder.draw import *
```
### Cut image area
```
get_area(binary_image: cv2.typing.MatLike, clip: tuple[int, int, int, int]) -> cv2.typing.MatLike
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
    text: str, font_path: str, font_size: int, stroke_width: int, kerning: int
) -> tuple[list[cv2.typing.MatLike], list[cv2.typing.MatLike]]
```
