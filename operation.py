
    # CREATE
    new_person = Person(name="Jagadeesh")
    new_person2=Person(name="aj")
    session.add(new_person)
    session.add(new_person2)
    session.commit()
    ##update
    res=session.get(Person,1149287437867581441)
    res.name="hero"
    session.commit()

    #get all 
    resi=session.query(Person).all()
    for i in resi:
        print(i.id,i.name)
    print("completed")

    #delete
    result=session.get(Person,1)
    session.delete(result)
    session.commit()
#these also delete like above line  stmt = delete(Person).where(Person.id == 1149284722270502913)
    #get all
    resi=session.query(Person).all()
    for i in resi:
        print(i.id,i.name)
"""