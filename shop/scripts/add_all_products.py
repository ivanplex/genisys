from shop.atomic.models import AtomicComponent, AtomicPrerequisite, AtomicSpecification, AtomicGroup
from shop.assembly.models import Blueprint, Product, ProductPrerequisite, ProductSpecification
from shop.models import URL, OffsetImageURL

import pandas as pd
import os


import time
###### Concept ######
# add atomic parts 
# blueprints are both SA and MAs
# Merge the tables
# build SA as blueprints 



    # get the SAs by ID
        # loop through
            # get_or_create prereqs
    # add prereqs
    # get_or_create specifications
        # loop through
            # get_or_create prereqs
    # add specs

# main assembly
    # repeat as per SA

def run():

    # SubAssemblies
    Parts               = pd.read_csv("shop\scripts\datafiles\Parts.csv")
    SubPartRelations    = pd.read_csv("shop\scripts\datafiles\SubPartRelations.csv")
    SubAssemblies       = pd.read_csv("shop\scripts\datafiles\SubAssemblies.csv")

    tables = {'Parts':Parts,'SubPartRelations':SubPartRelations,'SubAssemblies':SubAssemblies}

    for name, df in tables.items():
        # print(name, df)
        # time.sleep(5000)
        # df = Parts
        # df.name = 'Parts'
        # print (Parts.head())
        # Get ndArray of all column names 
        columnsNamesArr = df.columns.values
        listOfColumnNames = list(columnsNamesArr)
        # print(listOfColumnNames)
        # def renameCols(df):
        
        NewListOfColumnNames = []
        for col in listOfColumnNames:
            newcol = name + "__" + str(col)
            NewListOfColumnNames.append(newcol)

        # print(NewListOfColumnNames)
        dictionary = dict(zip(listOfColumnNames, NewListOfColumnNames))
        # print(dictionary)
        df.rename(columns=dictionary,inplace=True)
        # print(df.head())

    # print(Parts.head())

    # filter active
    # SubAssemblies = SubAssemblies[SubAssemblies['SubAssemblies__Deactivated'] == False] 

    # Merge df's    
    Merged = pd.merge(Parts, SubPartRelations, left_on='Parts__Id', right_on='SubPartRelations__Part_Id')
    Merged = pd.merge(Merged, SubAssemblies, left_on='SubPartRelations__Assembly_Id', right_on='SubAssemblies__Id')



    # print(Merged.head())

  
    Merged.to_csv('shop\scripts\datafiles\Merged.csv')





    # # GS-8-18 M6 M6 Parts


    # # BP

    # A BP is just an SA - but SA names are not uniquie so append the SA ID to the end of the nane 
    # Merged = pd.read_csv("shop\scripts\datafiles\Merged.csv")

    Merged['SA_Name'] = Merged["SubAssemblies__Name"]+ "#" + Merged["SubAssemblies__Id"].map(str)
    # Merged.to_csv('shop\scripts\datafiles\out.csv')
    Unique_SA = set(Merged['SA_Name'].unique().tolist())
    # print(Unique_SA)





    for SA in Unique_SA:
        print(f"{SA}  Parts:")
        print(f"     - create blueprint {SA} Parts")

        # Add Images
        # blueprint = Blueprint.objects.get_or_create(name=SA)[0]
        # blueprint.image_urls.add(URL.objects.get_or_create(url='https://dummyimage.com/300')[0])
        # blueprint.image_urls.add(URL.objects.get_or_create(url='https://dummyimage.com/200')[0])
        # blueprint.offset_image_urls.add(OffsetImageURL.objects.get_or_create(url='https://dummyimage.com/100',
        #                                                                     offset_x=3, offset_y=2)[0])





        # Get List of all parts in the SA
        df = Merged[Merged['SA_Name'] == SA]
        # print(df.head())
        

        print(df)


        def linkAtomicPrerequisite(row):

            try:
                if row['SubPartRelations__Amount'] == None:
                    partqty = 1
                else:
                    partqty = row['SubPartRelations__Amount']
                
                print (row['Parts__Id'])  
                AP = AtomicPrerequisite.objects.get_or_create(atomic_component=AtomicComponent.objects.filter(id=row['Parts__Id']).first(),
                min_quantity=partqty,
                max_quantity=partqty
                )[0]


                print (AP)

                return AP
            except expression as identifier:
                pass

          


        df.apply(linkAtomicPrerequisite, axis=1)

        # Parts = set(df['Parts__Id'].unique().tolist())
        # print(type(Parts))




        time.sleep(2)

        # for part in Parts:
        #     partqty = df['SubPartRelations__Amount'] 
        #     partid = df['Parts__Id'] 
        #     partname = df['Parts__sku']
        #     print(part,partid,partname)

            # GS_AP_1 = AtomicPrerequisite.objects.get_or_create(
            #     atomic_component=AtomicComponent.objects.filter(id=partid).first(),
            #     min_quantity=partqty,
            #     max_quantity=partqty
            # )[0]

    # ...for all parts in SA

    # blueprint.atomic_prerequisites.add(GS_AP_1)
    # time.sleep(5000)


    # # Product
