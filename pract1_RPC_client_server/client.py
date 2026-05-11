import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/api/v1/rpc_handler") as proxy:
    try:
        n = int(input("Enter a number: "))
        result = proxy.calculate_factorial(n)
        print(f"Factorial of {n} is: {result}")
    except Exception as e:
        print(f"Error: {e}")