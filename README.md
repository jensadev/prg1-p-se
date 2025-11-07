# En övning för programmering 1

Skapa en påse, ett inventory eller en "väska" att hålla saker i.

Vi kollar på sträng metoder, tex. lower() sidan 94 i boken.

Vi kollar på list metoder, se sidan 110 i boken.

## Material

Du har grunden som vi kodat tillsammans här i repot, app.py.
Använd den, läs igenom och se till att du förstår koden.
Det är främst repetition:
* spara, variabler och värden
* välja, if sats för att hantera menyn
* upprepa
  * while för huvudloopen, **eftersom vi inte vet antalet gånger vi ska upprepa**
  * for loop i visa menyn, **eftersom det är ett bestämt antal**
 
## Uppgift

Du ska testa att använda någon sträng metod och någon list metod.

Nu ska du utöka funktionen för väskan, du kan hitta på något eget eller göra någon av följande.
* Ta bort saker, för det använder du list metoder.
 * Kan du ta bort genom att skriva namnet på en sak? Python har list metoder för detta. Men du kan också använd "in" för att skapa ett villkor. Läs mer om in i kapitel 6 (viktig sak att kunna!).
 * Skriver du ut en lista med alla saker med nummer och sedan väljer du ett nummer för att ta bort?
    * Bra för att öva på att jobba med index platser i en lista.
* Det ser lite trist ut, emojis? (win + .)
    * Färger? https://www.geeksforgeeks.org/python/print-colors-python-terminal/
*  Max antal, det kan vara 10 st eller att alla items har en vikt (weight limit)
*  Skriv in flera saker och spara alla separat, "grej, moj, sak" blir 3 delar i listan.
*  Sortera påsen.

# Påsen 2.0 med grafik

Nu ska du göra en grafisk version av påsen med tkinter.
Använd app_gui.py som grund.

Du kan läsa mer om tkinter och kontroller här:
https://www.geeksforgeeks.org/python/python-gui-tkinter/

## Kom igång med tkinter

Du måste importera tkinter med:

```python
import tkinter as tk
```

Sedan kan du skapa ett fönster med:

```python
window = tk.Tk()
window.title("Påsen 🎒")
window.geometry("500x500")
```

För att köra fönstret så behöver du lägga till längst ner i koden:

```python
window.mainloop()
```

mainloop() är en funktion som körs hela tiden och väntar på att användaren ska göra något, t.ex. klicka på en knapp.

## En textlabel

En label är en text som visas i fönstret. Du kan skapa en label med följande kod:

```python
label = tk.Label(window, text="Välkommen till påsen!")  
label.pack()
```

Label() skapar en label och pack() lägger till den i fönstret. Label funktionen kräver två argument, fönstret där den ska visas och texten som ska visas.
Pack() är en metod som används för att placera kontrollen i fönstret. Det finns andra metoder för att placera kontroller, t.ex. grid() och place(), men pack() är den enklaste att använda. Du kan också ange en padding i pack() för att lägga till lite avstånd runt kontrollen, t.ex. pack(pady=10) för att lägga till 10 pixlar avstånd ovanför och under kontrollen.

```python
label.pack(pady=10)
```

## En knapp

Nu kan vi lägga till en knapp, den första vi gör är för att avsluta programmet.

```python
exit_button = tk.Button(window, text="Avsluta", command=window.quit)
exit_button.pack(pady=10)
```

Button() skapar en knapp och pack() lägger till den i fönstret. Button funktionen kräver tre argument, fönstret där den ska visas, texten som ska visas på knappen och kommandot som ska köras när knappen klickas. I detta fall är kommandot window.quit som avslutar programmet.

### En knapp för att visa saker i påsen

Vi kan nu testa att göra en knapp som kallar på en metod som vi själv har skapat. Vi behöver först skapa en metod för att visa saker i påsen, vi kan kalla den show_bag().
Först så kommer show_bag() bara använda koden från vårt konsol-program.

```python
def show_bag():
    print("Innehållet i påsen:")
    for item in bag:
        print(f"- {item}")
```

Sedan skapar vi en knapp som kallar på show_bag() när den klickas.

```python
show_button = tk.Button(window, text="Visa påsen", command=show_bag)
show_button.pack(pady=10)
```

Innan du testar programmet, se till att du har några saker i påsen, t.ex.

```python
bag = ["kompass", "ficklampa", "första hjälpen kit"]
```

## Lägga till saker i påsen med en input ruta

Nu ska vi göra en input ruta där användaren kan skriva in en sak som ska läggas till i påsen. Vi kan använda en Entry kontroll för detta.

```python
entry = tk.Entry(window)
entry.pack(pady=10)

def add_to_bag():
    item = entry.get()
    if item:
        bag.append(item)
        entry.delete(0, tk.END)
        print(f"{item} har lagts till i påsen.")
```

Här har vi skapat en funktion för att lägga till saker i påsen. Vi hämtar texten från input rutan med entry.get(), lägger till den i påsen med bag.append(item) och rensar input rutan med entry.delete(0, tk.END).

För att använda det så behöver vi knyta funktionen till en knapp. Det gör du på samma sätt som för show_bag() knappen.
Se om du kan lösa det, kom ihåg att knappen behöver ha kommandot add_to_bag.

## Visa saker i en text area

Nu ska vi lägga till en text area där vi kan visa innehållet i påsen. Vi kan använda en Text kontroll för detta.
Text kontrollen skapar ett område där vi kan visa flera rader med text.

```python
text_area = tk.Text(window, height=10, width=50)
text_area.pack(pady=10)

def show_bag():
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, "Innehållet i påsen:\n")
    for item in bag:
        text_area.insert(tk.END, f"- {item}\n")
```

Här har vi uppdaterat show_bag() funktionen för att visa innehållet i text_area istället för att skriva ut det i konsolen. Vi rensar först text_area med text_area.delete(1.0, tk.END) och sedan lägger vi till text med text_area.insert(tk.END, ...).

Nu kan du testa att köra programmet och använda knapparna för att lägga till saker i påsen och visa innehållet i text rutan.

## Extra utmaningar

* Lägg till en knapp för att ta bort saker från påsen.
* Lägg till en knapp för att sortera saker i påsen i alfabetisk ordning.
* Lägg till en etikett som visar antalet saker i påsen.
* Lägg till en knapp för att tömma påsen helt.
* Lägg till ikoner eller bilder för att göra gränssnittet mer attraktivt.

