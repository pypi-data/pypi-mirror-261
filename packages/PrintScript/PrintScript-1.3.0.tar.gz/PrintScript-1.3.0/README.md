# PrintScript

## Write less, do more


```python
import PrintScript.zpl as ZPL

# specify your image file path
imagePath = "/path/to/your/image.png"

with open("example.zpl", "wb") as file:

    # create a script generator
    generator = ZPL.Generator()

    # set parameters
    generator.setPrintWidth(576) \
             .setLabelLength(800) \
             .setLabelShift(0) \
             .setLabelHomePosition((0, 0)) \
             .addGraphicField((0, 0), (576, -1), imagePath)

    # generate the script
    script = generator.makeScript()

    # write it to the file
    file.write(script)
```
