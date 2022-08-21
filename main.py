from sp2400python import *

printer = sp2400python("COM1")

# printer.sendCommand(printer.DOUBLE_STRIKE_START)
# printer.sendCommand(printer.EMPHASIZED_START)
#
# printer.printLine("Zażółć gęślą jaźń")
# printer.printLine("ZAŻÓŁĆ GĘŚLĄ JAŹŃ")

fonts = {
    "NLQ": printer.FONT_NLQ,
    "SANS SERIF": printer.FONT_SANS_SERIF,
    "COURIER": printer.FONT_COURIER,
    "PRESTIGE": printer.FONT_PRESTIGE,
    "SCRIPT": printer.FONT_SCRIPT,
    "GOTHIC": printer.FONT_GOTHIC
}

printer.sendCommand(printer.QUALITY_NLQ)
for key in fonts:
    printer.setFont(fonts[key])
    printer.printLine("Font demo of: " + key)


# printer.sendCommand(printer.QUALITY_NLQ)
# printer.setFont(printer.FONT_SCRIPT)
# printer.sendCommand(printer.EMPHASIZED_START)
# printer.sendCommand(printer.DOUBLE_HEIGHT_START)
# printer.sendCommand(printer.DOUBLE_WIDTH_START)
# printer.printLine("DUŻY NAPIS")
# printer.sendCommand(printer.DOUBLE_HEIGHT_END)
# printer.sendCommand(printer.DOUBLE_WIDTH_END)

# printer.sendCommand(printer.DOUBLE_STRIKE_START)
# printer.sendCommand(printer.EMPHASIZED_START)
# printer.sendCommand(printer.PRINTING_UNIDIRECTIONAL)
# for i in range(5):
#     printer.printLine("TEST UNI")
#
# printer.sendCommand(printer.PRINTING_BIDIRECTIONAL)
# for i in range(5):
#     printer.printLine("TEST BI")

