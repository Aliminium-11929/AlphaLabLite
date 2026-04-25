# AlphaLabLite
# Setup
1. Clone the repository:
   `git clone https://github.com/Aliminium-11929/AlphaLabLite`
2. Set up a python virtual environment:
   `python -m venv venv`
3. Install dependencies
   `pip install requirements.txt`
4. Run the CLI or API app to get started.
   `python ./solution_cli.py` or `python ./solution_api.py`
---
# Initial Run
Running the CLI app with no arguments launches the help menu:
```bash
usage: solution_cli.py [-h] {execute,view} ...  
  
CLI tool  
  
positional arguments:  
 {execute,view}  
   execute       Read entire stdin as input script  
   view          View items by ID  
  
options:  
 -h, --help      show this help message and exit
```
Running the API app starts a Flask app at localhost port 8000.

---
# Usage
## CLI App:
- Launching the CLI app with the `execute` argument as above causes the terminal to wait for input, during which the user can input a script. When the user finishes the script, pressing CTRL + D causes the script to run, either raising a syntax error, or successfully running the script giving the following output: 
  `Script successfully executed: <Script-Output-ID>`
- Viewing the results of a script can be done by running the app using the `view` argument instead, passing the script ID and the variables whose values the user wants to view:
  `python ./solution_cli.py view --id <Script-Output-ID> variable_1 variable_2 ...`
## API App:
Running the command to launch the app launches a Flask app listening at port 8000. To send requests and get responses, users can use the curl command. Example:
```bash
curl -X 'POST' \
'http://127.0.0.1:8000/execute' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"script": "variable_1 = Fetch{OneMinuteBitcoinPrices}{}\nvariable_2 = Fetch{OneMinuteEthereum}{}"
}'
```
Running the above command sends input to the app in JSON format, which includes the script:
```
variable_1 = Fetch{OneMinuteBitcoinPrices}{}
variable_2 = Fetch{OneMinuteEthereum}{}
```
The app runs the above script, and sends back a JSON response as such:
`{"message": "Script successfully executed", "result": "<Script-Output-ID>"}`

To view the result of a script, the following curl command can be used:
```bash
curl -X 'GET' \
'http://0.0.0.0:8000/view/<Script-Output-ID>?items=variable_1&items=variable_2' \
-H 'accept: application/json'
```
In the above, replacing `<Script-Output-ID>` with the actual ID and filling in items referring to actual variable names defined within the script outputs the following JSON response:
`{"variable_1": [<CLIPPED>], "variable_2": [<CLIPPED>]}`

---
# Script Syntax
There are, in total, 7 transformations to be used within a script:
## Fetch 
Fetch transformation is the starting point of any script. It takes no input series and only one input configuration `datasource`. The file `fetch_transformation_data.csv` is a csv file in which each row is a uniquely labeled series. The Fetch transformation will return the series located in the row with the label corresponding to `datasource`.
- **Name:** Fetch
- **Input configurations (1)**
	- `$datasource$`: a unique label identifying which series to select 
- **Input series (0)**
- **Output:** the series located at the row labeled `$datasource$` in `fetch_transformation_data.csv`
## SimpleMovingAverage
Simple Moving Average is a denoising transformation that takes sliding window average of a series.
- **Name:** SimpleMovingAverage
- **Input configurations (1)**
	- `$window$`: the sliding average’s window
- **Input series (1)**
	-  $A$: the series to denoise.
- **Output:** $B$, a series where
$$
B[t] =
\begin{cases}
\sum_{i=t-window+1}^{t} \frac{A[i]}{window} & t \geq window - 1 \\
NaN & t < window - 1
\end{cases}
$$
*note: A and B are 0-indexed*
## ExponentialMovingAverage
Exponential Moving Average is another denoising transformation.
- **Name:** ExponentialMovingAverage
- **Input configurations (1)**
	- `$alpha$`: the smoothing factor
- **Input series (1)**
	- $A$: the series to denoise.
- **Output:** $B$, a series where
$$
B[t] =
\begin{cases}
alpha \times A[t]+(1-alpha) \times B[t-1] & t \geq  1 \\
A[t] & t = 0
\end{cases}
$$
## RateOfChange
Rate of Change transformation serves to quantify a change in the series given a period of time.
- **Name:** RateOfChange
- **Input configurations (1)**
	- `$period$`: a constant.
- **Input series (1)**
	- $A$: a series.
- **Output:** $B$, a series where
$$
B[t] =
\begin{cases}
\frac{A[t]-A[t-period]}{A[t-period]} & A[t-period] \neq 0 \\
NaN & A[t-period] = 0
\end{cases}
$$
## CrossAbove
Cross Above transformation is an indicator function that returns 1 when its first series crosses above its second series and 0 otherwise.
- **Name:** CrossAbove
- **Input configurations (0)**
- **Input series (2)**
	- $A_1$: a series.
	- $A_2$: a series.
- **Output:** $B$, a series where
$$
B[t] =
\begin{cases}
1.0 & A_1[t − 1] < A_2 [t − 1] \ and \ A_1 [t] > A_2 [t] \\
0.0 & otherwise
\end{cases}
$$
## ConstantSeries
Constant Series transformation is a helper to generate a constant series of the same length as another. This transformation is useful when paired with the cross above transformation or the rate of change transformation.
- **Name:** ConstantSeries
- **Input configurations (1)**
	- `$k$`: the constant
- **Input series (1)**
	- $A$: the reference series
- **Output:** $B$, a series of the same size as $A$, where
$$
B[t] = k
$$
## PortfolioSimulation
Portfolio Simulation transforms the price series, entry and exit signals into a series that tracks the portfolio’s net worth.
- **Name:** PortfolioSimulation
- **Input configurations (1)**
	- `$balance$`: the initial starting balance
- **Input series (3)**
	- $price$: the price series of an asset (e.g. Gold)
	- $entry$: the entry (buy) signal series
	- $exit$: the exit (sell) signal series
- **Output:** $portfolio$, constructed according to the following pseudo-code:
```
portfolio_simulation(balance, price, entry, exit)
	n = price.size
	positions_held = 0
	portfolio = float[n]
	for i in 0..n-1 (inclusive)
		if exit[i] = 1
			balance += positions_held * price[i]
		else if entry[i] = 1
			positions_held += 1
			balance -= price[i]
		portfolio[i] = balance + positions_held * price[i]
	return portfolio
```
---
# Formal Script Language Grammar
```
program = { ID "=" call "\n" } ;
call = ID "{" [args] "}" "{" [args] "}" ;
args = ID { "," ID } ;
ID = [A-Za-z0-9_]+ ;
```

---
# Example Usage
In this section, you will see the tool in action. Since the output might be too large to show here, it is clipped by denoting `<CLIPPED>`.
## Command Line Interface
### Example 1
```bash
$ python ./solution_cli.py    
usage: solution_cli.py [-h] {execute,view} ...  
  
CLI tool  
  
positional arguments:  
 {execute,view}  
   execute       Read entire stdin as input script  
   view          View items by ID  
  
options:  
 -h, --help      show this help message and exit
```
### Example 2
```
$ python ./solution_cli.py execute
price  = Fetch{OneMinuteGoldPrices}{}
fast   = ExponentialMovingAverage{0.3}{price}
slow   = SimpleMovingAverage{20}{price}
entry  = CrossAbove{}{fast, slow}
exit   = CrossAbove{}{slow, fast}
result = PortfolioSimulation{10000}{entry, exit, price}
^D
Script sucessfully executed: 14601f2a-d579-4a19-89eb-40aa3ed42fe9
```
```bash
$ python ./solution_cli.py view --id 14601f2a-d579-4a19-89eb-40aa3ed42fe9 price entry exit result
price:
	[1799.5677, <CLIPPED>, 1773.9234]
entry:
	[0.0, <CLIPPED>, 1.0, <CLIPPED>, 0.0]
exit:
	[0, <CLIPPED>, 1.0, <CLIPPED>]
result:
	[10000.0, <CLIPPED>, 10126.837]
```
## REST Interface
### Example 1: Execute
```bash
curl -X 'POST' \
'http://127.0.0.1:8000/execute' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"script": "btc = Fetch{OneMinuteBitcoinPrices}{}\neth = Fetch{OneMinuteEthereum}{}"
}'
{"message": "Script successfully executed", "result": "479f8db9-1b68-4a9f-bd5c-a5c7fef194d9"}
```
### Example 2: View

```bash
curl -X 'GET' \
'http://0.0.0.0:8000/view/479f8db9-1b68-4a9f-bd5c-a5c7fef194d9?items=btc&items=eth' \
-H 'accept: application/json'
{"btc": [<CLIPPED>], "eth": [<CLIPPED>]}
```
