import os

imagesPath = "Things_To_Play/"
doNotTouchPath = "DO_NOT_TOUCH/"

if(not os.path.exists(imagesPath)):
    os.makedirs(imagesPath)
if(not os.path.exists(doNotTouchPath)):
    os.makedirs(doNotTouchPath)

dir_list = os.listdir(imagesPath)

fullHTML = " "
allImages = " "

for file in dir_list:
    
    if(file.endswith(".mov")):
        image = """
        <video width="1920" class="mySlides fade" src="http://absolute/""" + os.path.dirname(__file__)+"/" + imagesPath + file + """">
                        
                        </video>
                        
                        
                        """
    else:
        image = """
            <div class="mySlides fade">
            <img src="http://absolute/""" + os.path.realpath(os.path.dirname(__file__))+"/" + imagesPath + file + """" style="width:100%" >
            </div>
            """
    allImages += image




def createHTML(images):
    return """ <!DOCTYPE html>
    <html>
        <head>
	        <meta charset="UTF-8" />
        </head>
        <body>
            <style>
                .slideshow-container {
                    max-width: 1920px;
                    position: relative;
                    margin: auto;
                    }
                .mySlides {
                    display: none;
                    }
                .fade {
                    animation-name: fade;
                    animation-duration: 1.5s;
                    }
                @keyframes fade {
                    from {opacity: .4}
                    to {opacity: 1}
                    }
            </style>

  </div>
            
        """ + images + """

            
        </div>
    <script>

        let slideIndex = 0;
        showSlides();

        function showSlides() {
            let i;
            let slides = document.getElementsByClassName("mySlides");
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
                }
            slideIndex++;
            if (slideIndex > slides.length) {slideIndex = 1}
            slides[slideIndex-1].style.display = "block";
            if (parseInt(slides[slideIndex-1].duration) < 1000){
                
                    slides[slideIndex-1].play()
                    setTimeout(showSlides, parseInt(slides[slideIndex-1].duration) * 1000);
                } else {
                setTimeout(showSlides, 30000);
                }
            
            
            }
    </script>
    </body>
    </html>"""

f = open(doNotTouchPath+ "browser.html", "w")

f.write(createHTML(allImages))
