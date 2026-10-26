from password_checker import check_password

print("=====================")
print("PASSWORD     STRENGTH")
print("=====================")

password=input("Enter your password:")

result=check_password(password)

print("\n---password Analysis---")
print("Strength:",result["strength"])
print("Score:",result["score"],"/6")

if result["suggestions"]:
    print("\n Suggestions:")

    for suggestion in result["suggestions"]:
        print("-",suggestion)
    else:
        print("\n Great! YOU PASSED ALL THE CHECKS")
