def printdetails():
    if __name__=="__main__":
        print("This is executing directly")
        name = 'Subash'
        noofdays=15
        year=2024
        print('Dear '+name+', \nYou have '+str(noofdays)+' days of leave balance for this \nyear('+str(year)+').')
    else:
        print("This is executing indirectly from other module")
        name = 'Subash'
        noofdays=15
        year=2024
        print('Dear '+name+', \nYou have '+str(noofdays)+' days of leave balance for this \nyear('+str(year)+').')

printdetails()
