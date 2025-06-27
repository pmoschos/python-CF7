
def main():
    months = ["Jan", "Feb", "Mar"]
    input_month = input("Please insert 3 letters for a month: ")
    
    # 1st way
    found = False
    for month in months:
        if month.casefold() == input_month.casefold():
            found = True
            break
    
    print(f"Input month found {input_month}"
          if found else f"Month: {input_month} not found") 
    
    # 2nd way
    for month in months:
        if month.casefold() == input_month.casefold():
            print(f"Input month found: {input_month}")
            break
    else:
        print(f"Month: {input_month} not found")

if __name__ == "__main__":
    main()