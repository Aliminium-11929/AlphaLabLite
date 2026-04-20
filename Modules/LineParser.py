from Model.RegEx import RegEx


def parse_line(scriptLine: str) -> RegEx:
    """Parses a line into the defined regular expression."""
    # Assuming line is in form: "varname = callname{inputConf}{inputSeries}"
    parsed_expression = RegEx()  # Fields: [varname, callname, inputConf, inputSeries]
    splitLine = scriptLine.split()
    # [varname, '=', call_expr (callname{inputConf}{inputSeries})]
    parsed_expression.varname = splitLine[0]
    call_expr = splitLine[2]
    n = len(splitLine)
    if n > 3:
        for i in range(3, n):
            call_expr += splitLine[i].strip()
    call_parameters = []
    regex_component = ""
    start = 0
    while start < len(call_expr):
        char = call_expr[start]
        if char != "{":
            regex_component += char
        else:
            if regex_component:
                call_parameters.append(regex_component)
            end = start + 1
            while call_expr[end] != "}":
                end += 1
            call_parameter = call_expr[start + 1 : end]
            call_parameters.append(call_parameter)
            start = end
            regex_component = ""
        start += 1
    # callparam is now an array of 3 elements: callname, inputConf as a string, inputSeries as a string
    parsed_expression.callname = call_parameters[0]

    # list of strings composing inputConf, keeping as list in case of adding new transformations taking more than 1 inputConf
    parsed_expression.inputConf = call_parameters[1].split(",")
    # No transformation takes more than one inputConf, splitting here currently does nothing but return the string as a list of 1 string.

    # list of strings composing inputSeries
    parsed_expression.inputSeries = call_parameters[2].split(",")

    return parsed_expression
