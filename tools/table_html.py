def create_table(data):
    keys = list(data.keys())

    tables = ""

    for i in range(len(data[keys[0]]) + 1):
        table = ""
        for j in range(len(keys)):
            if i == 0:
                table += str("<th>" + keys[j] + "</th>")
            else:
                table += str("<th>" + data[keys[j]][i - 1] + "</th>")
        tables += "<tr>" + table + "</tr>"

    tables = "<table>" + tables + "</table>"

    return tables


def create_table_rotate(data):
    keys = list(data.keys())

    tables = ""

    for i in range(len(keys)):
        table = ""
        for j in range(len(data[keys[0]]) + 1):
            if j == 0:
                table += str("<th>" + keys[i] + "</th>")
            else:
                table += str("<td>" + data[keys[i]][j - 1] + "</td>")
        tables += "<tr>" + table + "</tr>"

    tables = "<table>" + tables + "</table>"

    return tables
