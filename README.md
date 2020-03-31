# Searching-Text-In-Image
Searching A Text or Keyword in The Handwritten Scanned Pile of Images

Have you ever faced a problem in finding a text or keyword in the handwritten scanned pile of documents? And got frustrated for doing it manually? or, cursed yourself for doing such a job? Sometimes you might have cursed the technology too! for not making your job easier.

Anytime while doing this kind of work, did you thought or search on the internet is there any application that can solve your problem? If that so believe me, you were in the right place!

### Let’s breakdown our problem statement as execution steps,

- [x] Image Processing: Converting the scanned copy of the handwritten images into the machine-readable text. 
- [x] Search Keyword: Scanning the converted image to a text document to find given keywords.
- [x] Highlight Keyword: Highlighting the found keywords in a different color which helps the reader to read it fast. 
- [x] Restore Image: After the successful process of searching and highlighting store the image back to its original form.

### Pre-requisites 

- Tech stack: Python 
- Necessary Libraries:*
  - Image Processing	: Python Imaging Library (PIL) -- *Installation Assistance:  https://pypi.org/project/Pillow/2.2.2/*
  - Image to Text		: Tesseract -- *Installation Assistance:  https://pypi.org/project/pytesseract/*
  - Data Processing		: Pandas -- *Installation Assistance:  https://pypi.org/project/pandas/*

### Pseudo code

- Step 1: Input the Image repository and the keyword to highlight.
- step 2: Iterate each keyword, split each word in the keyword as a list.
- step 3: Now iterate keyword by keyword, in turn again word by word of that keyword.
- step 4:
  - A: Load the img by img in the repository 
  - B: Make a copy of the original img which will be helpful for rollback.
  - C: Iterate first word of the first keyword
  - D: Check whether the keyword present in the image 
    - IF,
      - D1: Highlight the word
      - D2: check the next concurrent word present next to next 
      - IF, 
          - D1.1: Highlight all the remaining following words 
       - Else,
          - D1.2: Rollback the img as org_img, since consecutive words not found 

After step 4, we will be successfully scanned the image for the keyword and highlighted if its presents

### How to run the code?

- [x] Loadpythonfile ImgTextScan.py
- [x] Input:
- Example Image File: testfilesample1.jpg # Construction Contract
- Keyword To Highlight: “Florida Department of Transportation”
- [x] Run the PY file 
- [x] Output Refer output.png img file

![Output](https://github.com/muthuvenki/Searching-Text-In-Image/blob/master/ocr/output.png)

### Conclusion 

This is just a sample that I’ve demoed. Further, we can use this in the different useful way of real-life business case problems like,
- 1.	Scanning a string in a scanned document of millions of images and find similarity documents.
- 2.	Finding a specific statement or quotation of large scanned books 

For any clarification in the codes or require different functionalities or if you have any different use case in similar lines, please feel free to contact me on ***venkatmuthiahc@gmail.com.***


