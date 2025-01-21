from django.shortcuts import render

def calcu(request):
    c = ''
    try:
        if request.method == 'POST':
            n1 = eval(request.POST.get('num1'))  # Convert to float
            n2 = eval(request.POST.get('num2'))  # Convert to float
            output = request.POST.get('output')

            if output == '+':
                c = n1 + n2
            elif output == '-':
                c = n1 - n2
            elif output == '*':
                c = n1 * n2
            elif output == '/':
                c = n1 / n2 if n2 != 0 else "Cannot divide by zero"
            else:
                c = "Invalid operator"
    except ValueError:
        c = "Invalid input"
    except Exception as e:
        c = f"Error: {e}"
    
    return render(request, "calculator.html", {'c': c})
