import datetime

# validations
date_str = input("Enter time to convert in 'YYYY-MM-DDThh:mm:ss±aa:bb' where T is the letter 'T', and aa:bb is the time zone offset from UTC:\n")
epoch_time = datetime.datetime.fromisoformat(date_str).timestamp()
print("_________________________________________________________________")
print("|\t\t\t|\t\t\t\t\t|")
print("| Paste this \t\t| To get this (in the viewer's time)\t|")
print("|_______________________|_______________________________________|")
print("|\t\t\t|\t\t\t\t\t|")
print("| <t:%d:d> \t| DD/MM/YYYY\t\t\t\t|" % epoch_time)
print("| <t:%d:D> \t| DD Month YYYY\t\t\t\t|" % epoch_time)
print("| <t:%d:t> \t| hh:mm\t\t\t\t\t|" % epoch_time)
print("| <t:%d:T> \t| hh:mm:ss\t\t\t\t|" % epoch_time)
print("| <t:%d:f> \t| DD Month YYYY hh:mm\t\t\t|" % epoch_time)
print("| <t:%d:F> \t| Day, DD Month YYYY hh:mm\t\t|" % epoch_time)
print("| <t:%d:R> \t| X minutes ago / in X minutes\t\t|" % epoch_time)
print("|_______________________|_______________________________________|")
