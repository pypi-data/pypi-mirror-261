# Simple-LaTeX-OCR
The encoder is resnetv2+simplevit, the decoder is transformer, the attention mechanism uses flashattention2.0 from pytorch2.0, and the dataset size is 112 million

Install the package `simplelatexocr`: 

```
pip install simplelatexocr
```

Use from within Python

    
    from simplelatexocr.models import Latex_OCR
    model = Latex_OCR()
    img_path = "tests/test_files/5.png"
    result = model.predict(img_path)
    print(result['formula'])
    print(result['confidence'])
    print(result['elapse'])
    
## Contribution
Contributions of any kind are welcome.

## Acknowledgment
Code taken and modified from [lukas-blecher](https://github.com/lukas-blecher/LaTeX-OCR), [RapidAI](https://github.com/RapidAI/RapidLaTeXOCR),[ultralytics](https://github.com/ultralytics/ultralytics)
