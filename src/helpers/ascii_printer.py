def ascii_printer():
    with open("/logo/logo.logo", "r") as f:
        art = f.read()
    print(art)
