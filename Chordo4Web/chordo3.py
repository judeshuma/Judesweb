

#define variables for comboboxes
values = ["C Major", "D Major", "E Major", "F Major", "G Major", "A Major", "B Major"]
values2 = [1, 2, 3, 4, 5, 6, 7]

label = Label(root, text="Choose Your Key Signature")
label.pack()
combo = ttk.Combobox(root, value=values)
combo.pack()

label = Label(root, text="Choose How Many Chords")
label.pack()
combo2 = ttk.Combobox(root, value=values2)
combo2.pack()

def chosen():
    values_C = ["C", "Dm", "Em", "F", "G", "Am", "Bb"]
    values_D = ["D", "Em", "F#m", "G", "A", "Bm", "C"]
    values_E = ["E", "F#m", "G#m", "A", "B", "C#m", "D"]
    values_F = ["F", "Gm", "Am", "Bb", "C", "Dm", "Eb"]
    values_G = ["G", "Am", "Bm", "C", "D", "Em", "F"]
    values_A = ["A", "Bm", "C#m", "D", "E", "F#m", "G"]
    values_B = ["B", "C#m", "D#m", "E", "F#", "G#m", "A"]
    
    final_list = []
    selection = request.form.get('keysig')
    numselection = request.form.get(int('numchords'))
    
    
    if "C Major" == selection:
        for i in range(0,numselection):
            num = random.randrange(numselection)
            chord = values_C.pop(num)
            numselection = numselection -1
            #final_list += [chord]
            final_list.append(chord)
            finale = str(final_list)
        print(f"{finale}")
        ffinale = print("Here are your chords: ", finale)
        

    elif "D Major" == selection:
        for i in range(0,numselection):
            dnum = random.randrange(numselection)
            dchord = values_D.pop(dnum)
            numselection = numselection -1
            #final_list += [dchord]
            final_list.append(dchord)
            finale = str(final_list)
        print(f"{finale}")
        ffinale = print("Here are your chords: ", finale)
        
    elif "E Major" == selection:
        for i in range(0,numselection):
            enum = random.randrange(numselection)
            echord = values_E.pop(enum)
            numselection = numselection -1
            #final_list += [echord]
            final_list.append(echord)
            finale = str(final_list)
        print(f"{finale}")
        ffinale = print("Here are your chords: ", finale)
        
    
    elif "F Major" == selection:
        for i in range(0,numselection):
            fnum = random.randrange(numselection)
            fchord = values_F.pop(fnum)
            numselection = numselection -1
            #final_list += [fchord]
            final_list.append(fchord)
            finale = str(final_list)
        print(f"{finale}")
        ffinale = print("Here are your chords: ", finale)
        

    elif "G Major" == selection:
        for i in range(0,numselection):
            gnum = random.randrange(numselection)
            gchord = values_G.pop(gnum)
            numselection = numselection -1
            #final_list += [gchord]
            final_list.append(gchord)
            finale = str(final_list)
        print(f"{finale}")
        ffinale = print("Here are your chords: ", finale)
        
    
    elif "A Major" == selection:
        for i in range(0,numselection):
            anum = random.randrange(numselection)
            achord = values_A.pop(anum)
            numselection = numselection -1
            #final_list += [dchord]
            final_list.append(achord)
            finale = str(final_list)
        print(f"{finale}")
        ffinale = print("Here are your chords: ", finale)
        
    
    elif "B Major" == selection:
        for i in range(0,numselection):
            bnum = random.randrange(numselection)
            bchord = values_B.pop(bnum)
            numselection = numselection -1
            #final_list += [bchord]
            final_list.append(bchord)
            finale = str(final_list)
        print(f"{finale}")
        ffinale = print("Here are your chords: ", finale)
        


    else:
        print("Nevermind")

def delete_everything():
    label2.destroy()

button = Button(root, text="Click Me For Chords", command=lambda:chosen()) 
button.pack()       

#button_clear = Button(root, text="Clean It Up!", command=lambda:delete_everything())
#button_clear.pack()

root.mainloop()



# How can i get the output to overwrite in the same place everytime
# How can i get the output to only print the final list and now the subsequent ones


#x = random.choice(values_C)
    #xnew = str(x)
    #xnewnew = print("Here is your chord: ", xnew)

# Can I create a variable for the input of what Major key and just have the code be one time and not have to repeat 5000 times thoroughout it?

# I still need to figure out how to not pull from a randrange too


#I need to add that layer to my list index, where as I can have the input select from the list of lists and use a variable globally for the input