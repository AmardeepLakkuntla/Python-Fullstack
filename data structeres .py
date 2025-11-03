players=["amar","shiva","arun","veera"]       #ists
print(players)                               
city=("sandeep","naveen","rohit")             #tuple
print(city)
citys=(players,["sandeep","Naveen","Rohit"])  #list outside tuple inside
print(citys)
villages=(city,{"players","sandeep"})         #list ouside set insede     
print(villages)
a={                                        
    "pavan":{9:"amar"}
}                               
print(a)


# a={                                   #outside dic key inside dic false
#     {"pavan"}:9  
# }                               
#  print(a)

# a={                                  #outside dictionory key inside list false
#     ["pavan"] :9  
# }                               
#  print(a)

# a={[1,2,3]}                            # outside set  inside List false                                
#  print(a)

# a={                                      # ouside set  inside dict false
#    {"towns":villages}
# }                                   
#  print(a)