# django-stickergen-telegram
A simple Django web-application that trasforms user's picture to suitable for a Telegram skicker format.

The idea behind the application is to simplify the creation of stickerpacks for Telegram users. Since Telegram's requirements for a sticker is pretty straightforward it's not difficult to define a set of rules for editing a picture to the format. User's iteraction will look like following:
1. User uploads their picture for a future sticker
2. User chooses an effect they want to add to their sticker (filters, blending with other pictures etc.)
3. After the picture is proccessed, user can download it and proceed the procedure in Telegram (there will be an explicit instruction on how to do that)
There also will be a statistics page for which I am going to use matplotlib package (as for now). Proccessing image implies applying chosen effects, croping it to the required size (512x512) and converting to .PNG if needed.

I primarily used PIL package for image proccessing. The project is built using Django, my DBMS choice is SQLite because I don't expect a loaded database.
