from django.shortcuts import render

def churn_rate(request):
    i = float(request.POST.get('initial', '0'))
    f = float(request.POST.get('final', '0'))

    churn = ((i - f) / i * 100) if request.method == 'POST' and i != 0 else 0

    print("initial customers =", i)
    print("final customers =", f)
    print("churn rate =", churn)

    return render(request, 'myapp/karthi.html',
                  {'i': i, 'f': f, 'churn': churn})