import tkinter as tk
from tkinter import ttk
import numpy as np
from sklearn import preprocessing
from tkinter import HORIZONTAL
LARGEFONT = ("Verdana", 35)
from tkinter import messagebox
from tkinter import filedialog
import matplotlib.pyplot as plt
global altlist
global altget
global goallist
global altdes
global crilist
global criget
global crides
global cridesget
global criimp
global criunit
global goalget
global goaldes
global goaldesget
global criunitget
global criimpget
global altdesget
global altvalue
global bestvalue


bestvalue=[]
altvalue=[]
altdesget=[]
criimpget=[]
criunitget=[]
goaldesget=[]
goaldes=[]
cridesget=[]
altget=[]
criget=[]
cridesget=[]
criunit=[]
altlist=[]
altdes=[]
goalget=[]
goallist=[]
crides=[]
crilist=[]
criimp=[]

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.grid()

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, ):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter


    def noaltcri(self, cont):
        global addaltnum
        addaltnum = int(str(noalt.get()))
        goaldesget.clear()
        goalget.clear()
        goallist.append(e1)
        goaldes.append(e2)
        for v in goaldes:
            goaldesget.append(str(v.get))
        for entries in goallist:
            goalget.append(str(entries.get))
        addcrinum = int(str(nocri.get()))

        class tkinterApp1(tk.Tk):

            # __init__ function for class tkinterApp
            def __init__(self, *args, **kwargs):
                # __init__ function for class Tk
                tk.Tk.__init__(self, *args, **kwargs)

                # creating a container
                container = tk.Frame(self)
                container.grid()

                container.grid_rowconfigure(0, weight=1)
                container.grid_columnconfigure(0, weight=1)

                # initializing frames to an empty array
                self.frames = {}

                # iterating through a tuple consisting
                # of the different page layouts
                for F in (Page2, Page4, Page5, Page6,Page7,):
                    frame = F(container, self)

                    # initializing frame of that object from
                    # startpage, page1, page2 respectively with
                    # for loop
                    self.frames[F] = frame

                    frame.grid(row=0, column=0, sticky="nsew")

                self.show_frame(Page2)





            # to display the current frame passed as
            # parameter

            def show_frame(self, cont):
                frame = self.frames[cont]

                frame.tkraise()
            def ensemble(self,cont,number):
                global addcrinum1
                global bestvalueget1
                global altvalueget1
                global maxminnormvalues1
                global eucnormarray1
                global altvalueget21

                global arraltvalue1
                global rank1list2
                rank1list2 = np.zeros(addaltnum)

                bestvalueget1 = np.zeros(addaltnum*addcrinum)
                altvalueget1 = np.zeros(addaltnum*addcrinum)
                maxminnormvalues1 = np.zeros(addaltnum*addcrinum)
                eucnormarray1 = np.zeros(addaltnum*addcrinum)

                altvalueget21 = np.zeros(addaltnum*addcrinum)
                for k in range(0,number):

                    for q in range(0,len(altvalue)):
                        altvalueget1[q] = np.random.normal(float(altvalue[q].get()), (float(altvalue[q].get()) / 10), 1)[0]
                        altvalueget21[q] = np.random.normal(float(altvalue[q].get()), (float(altvalue[q].get()) / 10), 1)[0]

                    maxminnormvalues1 = altvalueget21
                    maxminnormvalues1 = np.asarray(maxminnormvalues1)
                    maxminnormvalues1 = maxminnormvalues1.reshape(len(criget), len(altget)).T
                    min_max_scaler = preprocessing.MinMaxScaler()
                    maxminnormvalues1 = min_max_scaler.fit_transform(maxminnormvalues1)
                    eucnormarray1 = altvalueget21
                    eucnormarray1 = np.asarray(eucnormarray1)
                    eucnormarray1 = eucnormarray1.reshape(len(altget), len(criget)).T

                    summedup1 = np.zeros(len(altget))
                    for i in range(0, len(altget)):
                        for j in range(0, len(criimpget)):
                            summedup1[i] += (float((maxminnormvalues1[i][j])) * float(criimpget[j]))
                    for r in range(0, len(altget)):
                        if r == (summedup1.argmax()):
                            rank1list2[r] = rank1list2[r] + 1

                fig = plt.figure(figsize=(10, 5))

                # creating the bar plot
                plt.bar(altget, rank1list2, color='purple',
                        width=0.4)

                plt.xlabel("alternatives")
                plt.ylabel("number of times these were the best alternatives")
                plt.title("Ensemble")
                plt.show()

            def submitvalues(self, cont):
                global addcrinum
                global bestvalueget
                global altvalueget
                global maxminnormvalues
                global eucnormarray
                global altvalueget2

                global arraltvalue
                global rank1list

                rank1list = np.zeros(len(altget))

                bestvalueget = []
                altvalueget = []
                maxminnormvalues = []
                eucnormarray = []

                altvalueget2 = []
                altvalueget.clear()
                altvalueget2.clear()


                for a in altvalue:
                    altvalueget.append(float(a.get()))
                    altvalueget2.append(float(a.get()))
                maxminnormvalues=altvalueget2
                maxminnormvalues=np.asarray(maxminnormvalues)
                maxminnormvalues = maxminnormvalues.reshape( len(criget),len(altget)).T
                min_max_scaler = preprocessing.MinMaxScaler()
                maxminnormvalues = min_max_scaler.fit_transform(maxminnormvalues)
                eucnormarray=altvalueget2
                eucnormarray = np.asarray(eucnormarray)
                eucnormarray = eucnormarray.reshape(len(altget), len(criget)).T

                for b in bestvalue:
                    bestvalueget.append(float(b.get()))
            def plot(self,cont):

                crit=vara.get()

                x=np.arange(0,10.5,.5)
                criget2 = criimpget
                for i in range(0, len(altget)):
                    y = np.zeros(len(x))
                    for q in x:
                        criget2[criget.index(crit)] = q

                        for f in range(0, len(criimpget)):
                            y[np.where(x == q)] += (float((maxminnormvalues[i][f])) * float(criget2[f]))
                    plt.plot(x, y, label=altget[i])

                plt.xlabel("criteria weight")
                plt.ylabel("score")
                #plt.title("alternative scores with Varying weight of " + criget[criget.index(crit)])
                #fig = plt.figure(figsize=(5, 5))

                plt.legend()
                plt.show()



            def submitalt(self, cont):

                altdesget.clear()
                altget.clear()
                for a in altdes:
                    altdesget.append(a.get())
                for entries in altlist:
                    altget.append(str(entries.get()))



            def rank(self, cont):
                fig = plt.figure(figsize=(10, 5))

                # creating the bar plot
                plt.bar(altget, rank1list, color='purple',
                         width=0.4)

                plt.xlabel("alternatives")
                plt.ylabel("number of times these were the best alternatives")
                plt.title("sensitivity analysis")
                plt.show()

            def close(self, cont):
                self.destroy()

            def weightedsumcalculation(self, cont):
                global summedup1
                summedup1 = np.zeros(len(altget))
                for i in range(0, len(altget)):
                    for j in range(0, len(criimpget)):
                        summedup1[i] += (float((maxminnormvalues[i][j])) * float(criimpget[j]))

                fig = plt.figure(figsize=(10, 5))

                # creating the bar plot
                plt.bar(altget, summedup1, color='green',
                        width=0.4)

                plt.xlabel("alternatives")
                plt.ylabel("score")
                plt.title("alternative score")
                messagebox.showinfo('info', str(altget[summedup1.argmax()]) + ' is the best alternative')
                for r in range(0, len(altget)):
                    if r == (summedup1.argmax()):
                        rank1list[r] = rank1list[r] + 1
                plt.show()


                # plt.plot
                # plt.title
                # plt.xlabel
                # plt.show()

                # def addalt(self,cont,):

                # addcrinum =int(str(nocri.get()))





            def sliderchange(self,cont):
                global vertiscale
                vertiscale = criimp
                for i in range(0,len(criimpget)):

                    criimpget[i] =int(vertiscale[i].get())

                rank1list = np.zeros(len(altget))

                bestvalueget = []
                altvalueget = []
                maxminnormvalues = []
                eucnormarray = []

                altvalueget2 = []
                altvalueget.clear()
                altvalueget2.clear()

                for a in altvalue:
                    altvalueget.append(float(a.get()))
                    altvalueget2.append(float(a.get()))
                maxminnormvalues = altvalueget2
                maxminnormvalues = np.asarray(maxminnormvalues)
                maxminnormvalues = maxminnormvalues.reshape(len(criget), len(altget)).T
                min_max_scaler = preprocessing.MinMaxScaler()
                maxminnormvalues = min_max_scaler.fit_transform(maxminnormvalues)
                eucnormarray = altvalueget2
                eucnormarray = np.asarray(eucnormarray)
                eucnormarray = eucnormarray.reshape(len(altget), len(criget)).T

                for b in bestvalue:
                    bestvalueget.append(float(b.get()))

            def begin(self,cont):
                app = tkinterApp()
                app.mainloop()
                self.destroy()



            def submitcri(self, cont):
                criunitget.clear()
                cridesget.clear()
                criget.clear()
                criimpget.clear()
                for a in criunit:
                    criunitget.append(a.get())
                for b in criimp:
                    criimpget.append(float(b.get()))

                for c in crides:
                    cridesget.append(c.get())
                for entries in crilist:
                    criget.append(entries.get())


        class Page2(tk.Frame):
            def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                f3l2 = ttk.Label(self, text='                      ')
                f3l3 = ttk.Label(self, text='                       ')
                f3l4 = ttk.Label(self, text='                       ')
                # plus = ttk.Button(self, text='Add more alternatives',command=lambda: controller.addalt(Page2,addaltnum))
                l8 = ttk.Label(self, text='                       ')
                l9 = ttk.Label(self, text='                       ')
                l10 = ttk.Label(self, text='                      ')
                l11 = ttk.Label(self, text='                       ')
                l12 = ttk.Label(self, text='                       ')
                f3l5 = ttk.Label(self, text='Label')
                f3l6 = ttk.Label(self, text='Description')
                # f3prev = ttk.Button(self, text='Previous', )
                L2 = ttk.Label(self, text='Enter the Alternatives', font='Verdana 15')
                next2 = ttk.Button(self, text='next', command=lambda: controller.show_frame(Page4))
                abort = ttk.Button(self, text='Abort', command=lambda: controller.begin(self))
                submit = ttk.Button(self, text='submit', command=lambda: controller.submitalt(self))
                # back = ttk.Button(self, text='Previous', command=lambda: controller.show_frame(Page2))

                e3 = ttk.Entry(self, text='alternative')
                e4 = ttk.Entry(self, )


                for i in range(7, 7 + int(addaltnum)):

                    k = ttk.Label(self, text=i - 6)
                    k.grid(row=i, column=2)
                    e5 = ttk.Entry(self, text='alternative' + str(i))
                    e6 = ttk.Entry(self, text='description' + str(i))
                    e5.grid(row=i, column=3)
                    e6.grid(row=i, column=4)
                    altlist.append(e5)
                    altdes.append(e6)

                    i += 1

                # plus.grid(row=5, column=5)

                L2.grid(row=0, column=3)
                f3l3.grid(row=2)
                f3l4.grid(row=3)
                f3l2.grid(row=4)
                submit.grid(row=7, column=6)
                l8.grid(row=8 + addaltnum, )
                f3l5.grid(row=5, column=3)
                f3l6.grid(row=5, column=4)
                # controller.addalt(Page2)
                # e3.grid(row=6, column=3)
                l9.grid(row=12 + addaltnum)
                l10.grid(row=8 + addaltnum)
                l11.grid(row=9 + addaltnum)
                # altlist.append((e3))
                # altdes.append(e4)

                abort.grid(row=13 + addaltnum, column=5, padx=5, pady=5, )
                # back.grid(row=13 + addaltnum, column=1, padx=5, pady=5, )

                # e4.grid(row=6+addaltnum, column=4)
                next2.grid(row=13 + addaltnum, column=1, padx=5, pady=5, )

        class Page4(tk.Frame):
            def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                f3l2 = ttk.Label(self, text='                      ')
                f3l3 = ttk.Label(self, text='                       ')
                f3l4 = ttk.Label(self, text='                       ')
                # plus = ttk.Button(self, text='Add more alternatives',command=lambda: controller.addalt(Page2,addaltnum))
                l8 = ttk.Label(self, text='                       ')
                l9 = ttk.Label(self, text='                       ')
                l10 = ttk.Label(self, text='                      ')
                l11 = ttk.Label(self, text='                       ')
                l12 = ttk.Label(self, text='                       ')
                f3l5 = ttk.Label(self, text='Label')
                f3l6 = ttk.Label(self, text='Description')
                f3prev = ttk.Button(self, text='Previous', command=lambda: controller.show_frame(Page2))
                L2 = ttk.Label(self, text='Enter the Criterion', font='Verdana 15')
                next2 = ttk.Button(self, text='next', command=lambda: controller.show_frame(Page5))
                abort = ttk.Button(self, text='Abort', command=lambda: controller.close(self))
                importance = ttk.Label(self, text='Weights(on a scale of 1 to 10)')
                unit = ttk.Label(self, text='Unit')
                # back = ttk.Button(self, text='Previous', command=lambda: controller.show_frame(Page2))

                e5 = ttk.Entry(self, text='alternative')
                submit = ttk.Button(self, text='submit', command=lambda: controller.submitcri(self))

                e6 = ttk.Entry()

                for i in range(7, 7 + int(addcrinum)):
                    global clicked
                    clicked = tk.StringVar()
                    clicked.set('5')

                    k = ttk.Label(self, text=i - 6)
                    k.grid(row=i, column=2)

                    # Set the default value of the variable
                    drop = ttk.Entry(self, text=str(i))
                    e7 = ttk.Entry(self, text='Criterion' + str(i))
                    e8 = ttk.Entry(self, text='description' + str(i) + 'criterion')
                    unitentry = ttk.Entry(self, text='unit' + str(i) + 'unit', )

                    criimp.append(drop)
                    crilist.append(e7)
                    crides.append(e8)
                    criunit.append(unitentry)

                    unitentry.grid(row=i, column=5)

                    e7.grid(row=i, column=3)
                    e8.grid(row=i, column=4)
                    drop.grid(row=i, column=6)
                    i += 1

                # plus.grid(row=5, column=5)

                L2.grid(row=0, column=3)
                f3l3.grid(row=2)
                f3l4.grid(row=3)

                f3l2.grid(row=4)
                submit.grid(row=7, column=7)

                l8.grid(row=8 + addcrinum, )

                f3l5.grid(row=5, column=3)
                f3l6.grid(row=5, column=4)
                importance.grid(row=5, column=6)
                unit.grid(row=5, column=5)
                # controller.addalt(Page2)
                # e3.grid(row=6, column=3)

                l9.grid(row=12 + addcrinum)
                l10.grid(row=8 + addcrinum)
                l11.grid(row=9 + addcrinum)
                # altlist.append((e3))
                # altdes.append(e4)

                abort.grid(row=13 + addcrinum, column=5, padx=5, pady=5, )
                # back.grid(row=13 + addaltnum, column=1, padx=5, pady=5, )
                f3prev.grid(row=13 + addcrinum, column=1, padx=5, pady=5, )

                # e4.grid(row=6+addaltnum, column=4)
                next2.grid(row=13 + addcrinum, column=3, padx=5, pady=5, )

        class Page7(tk.Frame):
            def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                show = ttk.Button(self, text='show all criteria values', command=lambda: showallvalues(self))
                ensemble = ttk.Button(self, text='start', command=lambda: controller.ensemble(self, int(counts2.get())))
                counts=ttk.Label(self,text='enter number of counts')
                global counts2
                counts2=ttk.Entry(self,text='enter number of counts')
                show.grid(row=0)

                vertiscale = criimp

                def showallvalues(self, ):
                    k = 0
                    r = 0
                    t = 0

                    for cri in criget:
                        cwrite = ttk.Label(self, text=cri, font='verdana 12')
                        cwrite.grid(row=k + 2, column=3)
                        for r in range(0, len(altget)):
                            cvwrite = ttk.Label(self, text=altvalueget2[r + k * len(altget)], )
                            cvwrite.grid(row=k + 2, column=4 + r)
                            r += 1
                        k += 1

                    for alt in altget:
                        awrite = ttk.Label(self, text=alt, font='verdana 12')
                        awrite.grid(row=1, column=4 + t)
                        t += 1

                    weight = ttk.Label(self, text='Criteria weights', font='verdana 12')
                    prev = ttk.Button(self, text='Previous', command=lambda: controller.show_frame(Page6))
                    abort = ttk.Button(self, text='abort', command=lambda: controller.begin(self))
                    #weightedsum = ttk.Button(self, text='weighted sum model',
                                             #command=lambda: controller.weightedsumcalculation(self))
                    #sensi = ttk.Button(self, text='rank 1 count', command=lambda: controller.rank(self))

                    weight.grid(row=k + 2, column=1)
                    for cri in criget:
                        var = tk.StringVar()
                        var.set(int(criimp[criget.index(cri)].get()))
                        d = criget.index(cri)

                        cweightwrite = ttk.Label(self, text=cri, font='verdana 12')

                        cweightwrite.grid(row=k + 4, column=3)
                        verti = ttk.Scale(self, from_=(10-20), to=10, orient=HORIZONTAL, )
                        vertiscale[criget.index(cri)] = verti
                        l = verti.get()
                        apply = ttk.Button(self, text='apply', command=lambda: controller.sliderchange(self))
                        apply.grid(row=k + 4, column=5)
                        verti.set(var.get())
                        verti.grid(row=k + 4, column=4)  # orient=HORIZONTAL for horz slider

                        k += 1
                    prev.grid(row=k + 5, column=1)
                    #weightedsum.grid(row=k + 5, column=2)
                    #sensi.grid(row=k + 5, column=3)

                    abort.grid(row=k + 5, column=4)
                    ensemble.grid(row=k + 6, column=1)
                    counts.grid(row=k + 6, column=3)
                    counts2.grid(row=k + 6, column=2)

        class Page6(tk.Frame):
            def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                show = ttk.Button(self, text='show all criteria values', command=lambda: showallvalues(self))
                ensemble=ttk.Button(self, text='ensemble(gaussian)', command=lambda: controller.show_frame(Page7))
                show.grid(row=0)
                global vara
                vara=tk.StringVar()




                func=ttk.Button(self,text='alt scores with respect to varying weight of ',command= lambda:controller.plot(self))

                vertiscale = criimp




                def showallvalues(self, ):
                    k = 0
                    r = 0
                    t=0


                    for cri in criget:
                        cwrite = ttk.Label(self, text=cri, font='verdana 12')
                        cwrite.grid(row=k + 2, column=3)
                        for r in range(0,len(altget)):
                            cvwrite = ttk.Label(self, text=altvalueget2[r+k*len(altget)], )
                            cvwrite.grid(row=k + 2, column=4+r)
                            r+=1
                        k += 1


                    for alt in altget:
                        awrite = ttk.Label(self, text=alt, font='verdana 12')
                        awrite.grid(row=1, column=4 + t)
                        t += 1



                    weight = ttk.Label(self, text='Criteria weights', font='verdana 12')
                    prev = ttk.Button(self, text='Previous', command=lambda: controller.show_frame(Page5))
                    abort=ttk.Button(self, text='abort', command=lambda: controller.begin(self))
                    weightedsum=ttk.Button(self,text='weighted sum model',command=lambda:controller.weightedsumcalculation(self))
                    sensi=ttk.Button(self,text='rank 1 count',command=lambda:controller.rank(self))
                    optionmenu_a = ttk.OptionMenu(self, vara,criget[0],*criget)




                    weight.grid(row=k + 2, column=1)
                    for cri in criget:
                        var=tk.StringVar()
                        var.set(int(criimp[criget.index(cri)].get()))
                        d=criget.index(cri)

                        cweightwrite = ttk.Label(self, text=cri, font='verdana 12')

                        cweightwrite.grid(row=k + 4, column=3)
                        verti = ttk.Scale(self, from_=(10-20), to=10, orient=HORIZONTAL,)
                        vertiscale[criget.index(cri)]=verti
                        l=verti.get()
                        apply=ttk.Button(self,text='apply',command=lambda :controller.sliderchange(self))
                        apply.grid(row=k+4,column=5)
                        verti.set(var.get())
                        verti.grid(row=k + 4, column=4)  # orient=HORIZONTAL for horz slider

                        k += 1
                    prev.grid(row=k+5,column=1)
                    weightedsum.grid(row=k + 5, column=2)
                    sensi.grid(row=k+5,column=3)
                    abort.grid(row=k+5,column=4)
                    ensemble.grid(row=k+6,column=1)
                    func.grid(row=k+6,column=2)
                    optionmenu_a.grid(row=k+6,column=3)

        class Page5(tk.Frame):
            def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                i = 0

                show = ttk.Button(self, text='show', command=lambda: sizes(self))
                show.grid(row=1)

                def sizes(self):
                    t = 0
                    y = 1
                    k = 0
                    j = 0
                    submit = ttk.Button(self, text='submit', command=lambda: controller.submitvalues(self))
                    next = ttk.Button(self, text='next', command=lambda: controller.show_frame(Page6))
                    previous=ttk.Button(self, text='previous', command=lambda: controller.show_frame(Page4))

                    for x in criget:
                        l3 = ttk.Label(self, text='enter the values for ' + x)
                        k = int(t / 4)
                        l3.grid(row=2 + k * (len(altget) + 1), column=(3 * t) + 1 - 12 * k)


                        for i in altget:
                            check_1 = tk.IntVar()
                            l4 = ttk.Label(self, text=i)
                            valueentry = ttk.Entry(self, )
                            valueentry.grid(row=y + 2 + k * (len(altget) + 1), column=(3 * t) + 2 - 12 * k)
                            #c = ttk.Radiobutton(self, variable=check_1,value=1,command=lambda: controller.submitbestvalue(self,check_1) )
                            #c.grid(row=y + 2 + k * (len(altget) + 1), column=(3 * t) + 3 - 12 * k)
                            altvalue.append(valueentry)
                            bestvalue.append(check_1)

                            l4.grid(row=y + 2 + k * (len(altget) + 1), column=1 + (3 * t) - 12 * k)
                            y += 1
                            j += 1
                        y = 1
                        t += 1
                        submit.grid(row=j + k + 3, column=1)
                        previous.grid(row=j + k + 3, column=3)
                        next.grid(row=j + k + 3, column=2)

        app1 = tkinterApp1()

        app1.mainloop()


        # first window frame startpage

    #def nocrit(self,cont):

    def show_frame(self, cont):
        frame = self.frames[cont]

        frame.tkraise()
    def close(self, cont):
        self.destroy()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Startpage", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        L = ttk.Label(self, text='Multi Criteria Decision Analysis', font='Verdana 15')
        wizard = ttk.Button(self, text='wizard', command=lambda: controller.show_frame(Page1))
        load = ttk.Button(self, text='load',)
        #rimport = ttk.Button(self, text='import', )
        #process = ttk.Button(self, text='process', )
        #history = ttk.Button(self, text='history', )
        exit = ttk.Button(self, text='exit',command=lambda: controller.close(self) )
        L.grid(row=1,padx=15,pady=20)
        wizard.grid(row=2, padx=15, pady=20,)
        #load.grid(row=3, padx=15, pady=20)
        #rimport.grid(row=4, padx=15, pady=20)
        #process.grid(row=5, padx=15, pady=20)
        #history.grid(row=6, padx=15, pady=20)
        exit.grid(row=7, padx=15, pady=20)

# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #label = ttk.Label(self, text="Page 1", font=LARGEFONT)

        l1 = ttk.Label(self, text='Enter your goal',font='Verdana 15')
        l2 = ttk.Label(self, text='                      ')
        l3 = ttk.Label(self, text='                       ')
        l4 = ttk.Label(self, text='                       ')
        l7 = ttk.Label(self, text='                      ')
        l8 = ttk.Label(self, text='                       ')
        sub= ttk.Button(self, text='submit and next',command=lambda: controller.noaltcri(self))
        l10 = ttk.Label(self, text='                      ')
        l11 = ttk.Label(self, text='                       ')
        l12 = ttk.Label(self, text='                       ')
        l5 = ttk.Label(self, text='Label')
        l6 = ttk.Label(self, text='Description')
        global noaltnum
        noalt1 = ttk.Label(self, text='Enter number of alternatives')
        global noalt
        #nocri1 = ttk.Label(self, text='Enter number of criterion')
        noalt=ttk.Entry(self,text='0' )
        #noalt.insert(0,a)
        global nocrinum
        # noalt1 = ttk.Label(self, text='Enter number of alternatives')
        # global noalt
        global nocri

        nocri1 = ttk.Label(self, text='Enter number of criterion')
        # noalt=ttk.Entry(self,text='0' )
        # noalt.insert(0,a)

        nocri = ttk.Entry(self, text='1')
        # nocri.insert(0, b)
        nocri1.grid(row=8, column=4)
        # noalt1.grid(row=8,column=4)
        nocri.grid(row=9, column=4)
        # noalt.grid(row=9, column=4)

        #nocri=ttk.Entry(self,text='0' )
        #nocri.insert(0, b)
        global e1
        global e2


        e1 = ttk.Entry(self, )

        e2 = ttk.Entry(self, )


        abort = ttk.Button(self, text='Abort', command=lambda: controller.show_frame(StartPage))
        #next1 = ttk.Button(self, text='next',command=lambda: controller.show_frame(Page3))#
        #next1.grid(row=12, column=4, )
        l1.grid(row=1, column=4)
        l3.grid(row=2)
        l4.grid(row=3)
        l2.grid(row=4)
        l7.grid(row=10)
        l8.grid(row=11)
        sub.grid(row=12)
        #nocri1.grid(row=8,column=4)
        noalt1.grid(row=10,column=4)
        #nocri.grid(row=9, column=4)
        noalt.grid(row=11, column=4)
        l12.grid(row=10)
        l5.grid(row=5, column=4)
        l6.grid(row=5, column=5)

        e1.grid(row=6, column=4)
        e2.grid(row=6, column=5)
        #next1.grid(row=12, column=4,padx=5, pady=5, )
        abort.grid(row=12, column=9,padx=5, pady=5,)


app = tkinterApp()
app.geometry('400x400')
app.mainloop()
