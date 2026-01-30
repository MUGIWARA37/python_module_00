def   ft_seed_inventory(name , num , type) -> None :
    if(type == "packets"):
        print(name.capitalize(), "seeds:" ,num ,type ,"available")
    elif (type == "grams"):
        print(name.capitalize() , "seeds:" , num ,type , "total")
    elif (type == "area"):
        print(name.capitalize() , "seeds:" , num , "square meters")