def main():
    
    # know if user is a VIP 
    
    isVIP = int(input("If you're a VIP press 1 else press 0: ")) == 1
    
    # # VIP logic
    
    # if isVIP == 1:
    #     isVIP = True
    # else:
    #     isVIP = False                      this logic , is done by isVIP = expression() == 1
    
    if isVIP:
        print("Access Alwyas Allowed")
        
    else:
        age = int(input("How Old are you?: "))
        has_ticket = int(input("if you have a ticket press 1 lese press 0 : ")) == 1
        
        # # has_ticket logic
        # if has_ticket == 1:
        #     has_ticket = True
        # else:
        #     has_ticket = False        Same as for isVIP
            
        # rest of the logic
        if age >= 18 and has_ticket:
            print("Allowed")
        elif age < 18 and has_ticket:
            print("Restrictes")
        else:
            print("Denied")
    
    
main()