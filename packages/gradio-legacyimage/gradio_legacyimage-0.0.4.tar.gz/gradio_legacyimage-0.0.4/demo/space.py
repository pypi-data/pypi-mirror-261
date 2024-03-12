
import gradio as gr
from app import demo as app
import os

_docs = {'LegacyImage': {'description': 'Creates an image component that can be used to upload images (as an input) or display images (as an output).', 'members': {'__init__': {'value': {'type': 'str | PIL.Image.Image | numpy.ndarray | None', 'default': 'None', 'description': 'A PIL LegacyImage, numpy array, path or URL for the default value that LegacyImage component is going to take. If callable, the function will be called whenever the app loads to set the initial value of the component.'}, 'height': {'type': 'int | None', 'default': 'None', 'description': 'Height of the displayed image in pixels.'}, 'width': {'type': 'int | None', 'default': 'None', 'description': 'Width of the displayed image in pixels.'}, 'image_mode': {'type': '"1"\n    | "L"\n    | "P"\n    | "RGB"\n    | "RGBA"\n    | "CMYK"\n    | "YCbCr"\n    | "LAB"\n    | "HSV"\n    | "I"\n    | "F"', 'default': '"RGB"', 'description': '"RGB" if color, or "L" if black and white. See https://pillow.readthedocs.io/en/stable/handbook/concepts.html for other supported image modes and their meaning.'}, 'type': {'type': '"numpy" | "pil" | "filepath"', 'default': '"numpy"', 'description': 'The format the image is converted to before being passed into the prediction function. "numpy" converts the image to a numpy array with shape (height, width, 3) and values from 0 to 255, "pil" converts the image to a PIL image object, "filepath" passes a str path to a temporary file containing the image.'}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.'}, 'every': {'type': 'float | None', 'default': 'None', 'description': "If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute."}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will display label.'}, 'show_download_button': {'type': 'bool', 'default': 'True', 'description': 'If True, will display button to download image.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will allow users to upload and edit an image; if False, can only be used to display images. If not provided, this is inferred based on whether the component is used as an input or output.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'streaming': {'type': 'bool', 'default': 'False', 'description': "If True when used in a `live` interface, will automatically stream webcam feed. Only valid is source is 'webcam'."}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'mirror_webcam': {'type': 'bool', 'default': 'True', 'description': 'If True webcam will be mirrored. Default is True.'}, 'show_share_button': {'type': 'bool | None', 'default': 'None', 'description': 'If True, will show a share icon in the corner of the component that allows user to share outputs to Hugging Face Spaces Discussions. If False, icon does not appear. If set to None (default behavior), then the icon appears if this Gradio app is launched on Spaces, but not otherwise.'}, 'source': {'type': '"upload" | "webcam" | "canvas"', 'default': '"upload"', 'description': None}, 'invert_colors': {'type': 'bool', 'default': 'False', 'description': None}, 'shape': {'type': 'tuple[int, int] | None', 'default': 'None', 'description': None}, 'tool': {'type': '"editor" | "select" | "sketch" | "color-sketch" | None', 'default': 'None', 'description': None}, 'brush_radius': {'type': 'float | None', 'default': 'None', 'description': None}, 'brush_color': {'type': 'str', 'default': '"#000000"', 'description': None}, 'mask_opacity': {'type': 'float', 'default': '0.7', 'description': None}}, 'postprocess': {'y': {'type': 'PreprocessData | None', 'description': None}, 'value': {'type': 'PreprocessData | None', 'description': None}}, 'preprocess': {'return': {'type': 'PreprocessData | None', 'description': "The preprocessed input data sent to the user's function in the backend."}, 'value': None}}, 'events': {'clear': {'type': None, 'default': None, 'description': 'This listener is triggered when the user clears the LegacyImage using the X button for the component.'}, 'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the LegacyImage changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'stream': {'type': None, 'default': None, 'description': 'This listener is triggered when the user streams the LegacyImage.'}, 'select': {'type': None, 'default': None, 'description': 'Event listener for when the user selects or deselects the LegacyImage. Uses event data gradio.SelectData to carry `value` referring to the label of the LegacyImage, and `selected` to refer to state of the LegacyImage. See EventData documentation on how to use this event data'}, 'upload': {'type': None, 'default': None, 'description': 'This listener is triggered when the user uploads a file into the LegacyImage.'}, 'edit': {'type': None, 'default': None, 'description': 'This listener is triggered when the user edits the LegacyImage (e.g. image) using the built-in editor.'}}}, '__meta__': {'additional_interfaces': {'PreprocessData': {'source': 'class PreprocessData(TypedDict):\n    back: Optional[Union[np.ndarray, _Image.Image, str]]\n    mask: Optional[Union[np.ndarray, _Image.Image, str]]'}}, 'user_fn_refs': {'LegacyImage': ['PreprocessData']}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_legacyimage`

<div style="display: flex; gap: 7px;">
<a href="https://pypi.org/project/gradio_legacyimage/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_legacyimage"></a>  
</div>

Python library for easily interacting with trained machine learning models
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_legacyimage
```

## Usage

```python
import numpy as np

import gradio as gr
from gradio_legacyimage import LegacyImage

def process(x):
    flip = x.copy()
    flip["back"] = np.fliplr(flip["back"])
    mask = x.copy()
    mask["back"] = mask["mask"]
    return x, flip, mask

with gr.Blocks() as demo:
    with gr.Column():
        im1 = LegacyImage(source="upload", type="pil", tool="sketch")
        im2 = LegacyImage()
        im3 = LegacyImage()
        im4 = LegacyImage()

    btn = gr.Button()
    btn.click(process, inputs=im1, outputs=[im2, im3, im4])

if __name__ == "__main__":
    demo.launch()

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `LegacyImage`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["LegacyImage"]["members"]["__init__"], linkify=['PreprocessData'])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["LegacyImage"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, the preprocessed input data sent to the user's function in the backend.


 ```python
def predict(
    value: PreprocessData | None
) -> PreprocessData | None:
    return value
```
""", elem_classes=["md-custom", "LegacyImage-user-fn"], header_links=True)




    code_PreprocessData = gr.Markdown("""
## `PreprocessData`
```python
class PreprocessData(TypedDict):
    back: Optional[Union[np.ndarray, _Image.Image, str]]
    mask: Optional[Union[np.ndarray, _Image.Image, str]]
```""", elem_classes=["md-custom", "PreprocessData"], header_links=True)

    demo.load(None, js=r"""function() {
    const refs = {
            PreprocessData: [], };
    const user_fn_refs = {
          LegacyImage: ['PreprocessData'], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
