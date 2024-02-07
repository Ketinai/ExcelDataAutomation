```bash
pyenv virtualenv 3.10.7 kasia
pyenv activate kasia

pip install --upgrade pip
pip install -r requirements.txt
```

Example usage:
```bash
(kasia)  ~/CodeProjects/kasia_studia/ python main.py --filename ./Exampledata.xlsx --sheet Arkusz1 --index0 B2:E2 --operation s_sum
Loading: ./Exampledata.xlsx
Performing operation: s_sum <class 'myproject.operations.SingleSum'>
Result: 17771629
```

```bash
(kasia)  ~/CodeProjects/kasia_studia/ python main.py --filename ./Exampledata.xlsx --sheet Arkusz1 --index0 B3:E3 --operation if_sum --index_if C2 --condition CHF
Loading: ./Exampledata.xlsx
Performing operation: if_sum <class 'myproject.operations.ConditionalSum'>
RuntimeError: Condition != does not match!
```

```bash
(kasia)  ~/CodeProjects/kasia_studia/ python main.py --filename ./Exampledata.xlsx --sheet Arkusz1 --index0 B3:E3 --operation if_sum --index_if H6 --condition CHF
Loading: ./Exampledata.xlsx
Performing operation: if_sum <class 'myproject.operations.ConditionalSum'>
Result: 6
```

File saving:
```bash
(kasia)  ~/CodeProjects/kasia_studia/ python main.py --filename ./Exampledata.xlsx --sheet Arkusz1 --index0 B3:E3 --operation s_sum --save True
Loading: ./Exampledata.xlsx
Performing operation: s_sum <class 'myproject.operations.SingleSum'>
Updated file f./Exampledata.xlsx with column:
   Przychody:   I kwartał  II kwartał  III kwartał  IV kwartał Waluta  Kurs Walut  Results
0   Januszex    17716871       54758       658589   564654567    PLN    1.000000       10
1   Grażynex           1           4            2           3    PLN    2.500000       10
2   Mirekpol    57859759       45647        76576        5747    PLN    1.000000       10
3  Mirabelle  7858675646      654654         5476   212342353    EUR    1.105681       10
4  Szwindler    45345354      654654       542542     4564567    CHF    5.000000       10
Result: 10
(kasia)  ~/CodeProjects/kasia_studia/ 
```
```bash
(kasia)  ~/CodeProjects/kasia_studia/ python main.py --filename ./Exampledata.xlsx --sheet Arkusz1 --index0 B2:E2 --operation s_sum --save True --save_index 9 --save_name new_results 
Loading: ./Exampledata.xlsx
Performing operation: s_sum <class 'myproject.operations.SingleSum'>
Updated file f./Exampledata.xlsx with column:
    Unnamed: 0 Przychody:   I kwartał  II kwartał  III kwartał  IV kwartał Waluta  Kurs Walut  Results  new_results
0           0   Januszex    17716871       54758       658589   564654567    PLN    1.000000       10     18430218
1           1   Grażynex           1           4            2           3    PLN    2.500000       10     18430218
2           2   Mirekpol    57859759       45647        76576        5747    PLN    1.000000       10     18430218
3           3  Mirabelle  7858675646      654654         5476   212342353    EUR    1.105681       10     18430218
4           4  Szwindler    45345354      654654       542542     4564567    CHF    5.000000       10     18430218
Result: 18430218
```

Pivot:
```bash
(kasia)  ~/CodeProjects/kasia_studia/ python main.py --filename ./Exampledata.xlsx --sheet Arkusz1 --operation pivot --pivot_names "I kwartał" "II kwartał" "III kwartał" "IV kwartał" --pivot_index "Kurs Walut"
Loading: ./Exampledata.xlsx
Performing operation: pivot <class 'myproject.operations.PivotOperation'>
<class 'myproject.operations.PivotOperation'>
Result:              I kwartał  II kwartał  III kwartał  IV kwartał
Kurs Walut                                                 
1.000000      37788315     50202.5     367582.5   282330157
1.105681    7858675646    654654.0       5476.0   212342353
2.500000             1         4.0          2.0           3
5.000000      45345354    654654.0     542542.0     4564567
23.908000        44567     12123.0     647567.0      647648
32.568000       475476    654654.0      54654.0      654654
```
Saving pivot:
```bash
(kasia)  ~/CodeProjects/kasia_studia/ python main.py --filename ./Exampledata.xlsx --sheet Arkusz1 --operation pivot --pivot_names "I kwartał" "II kwartał" "III kwartał" --pivot_index "Kurs Walut" --save True
Loading: ./Exampledata.xlsx
Performing operation: pivot <class 'myproject.operations.PivotOperation'>
<class 'myproject.operations.PivotOperation'>
Created new file with pivot table!
Result:              I kwartał  II kwartał  III kwartał
Kurs Walut                                     
1.000000      37788315     50202.5     367582.5
1.105681    7858675646    654654.0       5476.0
2.500000             1         4.0          2.0
5.000000      45345354    654654.0     542542.0
23.908000        44567     12123.0     647567.0
32.568000       475476    654654.0      54654.0
(kasia)  ~/CodeProjects/kasia_studia/ ls
Exampledata.xlsx  README.md         main.py           myproject         report_pivot.xlsx requirements.txt
```