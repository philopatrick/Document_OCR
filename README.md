## Document OCR

This project is for scan the handwritten document, and transform them into text files. By using the latest deep learning models (**CRAFT** for text detection, **TROCR** for OCR transformation). This combinations can achieve very accurate results than other methods. Especially, the transformer OCR could both care about the individual word form but also the context information in the visual representation which can result better results than other methods. Related information, please read their papers()

## Set up
For GPU use
```bash
conda env create -n docOCR --file environment.yml  
```
For CPU use
```bash
conda env create -n docOCR --file environment-cpu.yml  
```

## The normal steps to do document ocr

The single OCR model cannot automatically convert a whole page of text image into the text forms. That's not the way normal ocr model work. Usually, because of trainning limitation, the model can only convert **one word** or **one line of words** into its' text forms. So, before we want to do a whole page of document ocr, we need to **detect the location of the word** or **the location of the whole line words**.


### FIRST STEP, measure and crop page
So, the first step is to detect word location, here we use **CRAFT-pytorch** project, which is a word detection project, it can do one single word location detection and with their **refiner model** to detect a line of words(But, it is not very good perfermance in line text detection).


*Here is one example document under processing*
![image](asset/front.png)

Although you can see, when we have some normal page, there still have some unwanted part in a page, so we can use some tools to crop the page. You can use `./utils/image_measure.py` to measure the point pixel position, and later use `./utils/image_crop.py` to crop the image.

*After croped the image, we have the interest part we care as follow.*
![image2](asset/crop_front.png)

If all your images in a folder have a similiar layout, you can use the `process_folder` function to process them all. However this maybe can be done with some other deep learning model with layout guessing ability(TODO).


### SECOND STEP, detect the word in document

You can detect the the image with `CRAFT-pytorch\test_raw.py`
use:
    ```bash
    python test_raw.py --trained_model=CRAFT-pytorch\craft_mlt_25k.pth --test_folder=CRAFT-pytorch\testimgraw --text_threshold=0.
    ```
here is the result:
![img3](asset/res_crop_image.jpg)


However you can directly load those cropped detected word into the OCR model. But this usually doesn't promise you a good result, cause it is just individual word lost the context.

So, I reform a little bit to use the word detection to the line detection. I join the whole line of word detection into lines of bounding boxes like below:
![img4](asset/res_crop_image_5.jpg)



### THIRD STEP, OCR

You can pass the folder contain the cropped images in `CRAFT-pytorch\test.py`

```python
## pass the folder path
images_all = glob.glob(r"D:\NLP\语料\语料\**\**\**\CroppedImage.png")
```

And then run with:
```bash
python test.py --trained_model=CRAFT-pytorch\craft_mlt_25k.pth --test_folder=CRAFT-pytorch\testimg --text_threshold=0.7
```

And then the Recognized text are stored in each image path folder in txt extention.
![img5](asset/OCR_Result_txt.png)


## Remind

This script is write in a mess, there are many parameters can be tuned, if you have any problem contact me.








