import random
import argparse
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet

def produceOutputFile(prefix, topmostImage, number, choices):
    filename = "{prefix}-{number}.pdf".format(prefix=prefix, number=number)

    # creating a pdf object 
    pdf = canvas.Canvas(filename, pagesize=letter) 
    pageWidth, pageHeight = letter

    # setting the title of the document 
    pdf.setTitle("Bingo!") 

    # Draw the topmost image.  This obviously assumes a specific image size.
    centerImageWidth = int(959/2.5)
    centerImageHeight = int(317/2.5)
    pdf.drawInlineImage(topmostImage, pageWidth/2-(centerImageWidth/2), pageHeight-20-centerImageHeight, 
                        width=centerImageWidth,
                        height=centerImageHeight) 
    styles = getSampleStyleSheet()
    normalStyleCentered = styles["Normal"]
    normalStyleCentered.alignment = 1
    normalStyleCentered.fontSize = 14
    normalStyleCentered.leading = 16

    p = Paragraph("Find the guest who matches the description and write their name down on the "
                  "square.  The first one with 5 in a row, wins!", normalStyleCentered)
    paragraphXOffset = 100
    p.wrapOn(pdf, pageWidth - (2*paragraphXOffset), 140)
    p.drawOn(pdf, paragraphXOffset, pageHeight-60-centerImageHeight)

    # Image occupying the center square has been hard coded here. 
    boxImage = Image("box.png")
    boxImage.drawHeight = int(boxImage.drawHeight/4)
    boxImage.drawWidth = int(boxImage.drawWidth/4)
      
    # Create a 5x5 table
    tableXOffset = 20
    tableYOffset = pageHeight-70-centerImageHeight 

    # Manual build of the grid utilizing Paragraph objects along with the Image object.
    grid = [[ Paragraph(choices[0],normalStyleCentered), Paragraph(choices[1],normalStyleCentered), Paragraph(choices[2],normalStyleCentered), Paragraph(choices[3],normalStyleCentered), Paragraph(choices[4],normalStyleCentered) ], 
            [ Paragraph(choices[5],normalStyleCentered), Paragraph(choices[6],normalStyleCentered), Paragraph(choices[7],normalStyleCentered), Paragraph(choices[8],normalStyleCentered), Paragraph(choices[9],normalStyleCentered) ], 
            [ Paragraph(choices[10],normalStyleCentered), Paragraph(choices[11],normalStyleCentered), boxImage,  Paragraph(choices[12],normalStyleCentered), Paragraph(choices[13],normalStyleCentered) ], 
            [ Paragraph(choices[14],normalStyleCentered), Paragraph(choices[15],normalStyleCentered), Paragraph(choices[16],normalStyleCentered), Paragraph(choices[17],normalStyleCentered), Paragraph(choices[18],normalStyleCentered) ], 
            [ Paragraph(choices[19],normalStyleCentered), Paragraph(choices[20],normalStyleCentered), Paragraph(choices[21],normalStyleCentered), Paragraph(choices[22],normalStyleCentered), Paragraph(choices[23],normalStyleCentered) ]]

    tableCellSize = (pageWidth-(tableXOffset*2))/5
    table = Table(grid, colWidths=tableCellSize, rowHeights=tableCellSize)
    table.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                ("ALIGN", (0,0), (-1,-1), "CENTER"),
                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                ('OUTLINE', (0,0), (-1,-1), 0.25, colors.black)])
    table.wrapOn(pdf, pageWidth, pageHeight)
    table.drawOn(pdf, tableXOffset, 10)

    pdf.save() 


ap = argparse.ArgumentParser()
ap.add_argument("-c", "--count", required=False, default = 1, type = int, help="Number bingo cards to produce")
ap.add_argument("-f", "--file", required=False, default = "choices.txt", type = str, help="File containing choices to show inside of squares")
ap.add_argument("-t", "--topimage", required=False, default = "AD.png", type = str, help="Image filename to show at the top of a bingo card")
ap.add_argument("-s", "--seed", required=False, default = 0, type = int, help="Seed value used for random number generator")
ap.add_argument("-o", "--output", required=False, default = "bingo", type = str, help="Output file prefix")
args = vars(ap.parse_args())

random.seed(args["seed"])

with open(args["file"]) as file:
    choices = [line.rstrip() for line in file]

for x in range(args["count"]):
    produceOutputFile(args["output"], args["topimage"], x, random.sample(choices, 24))
