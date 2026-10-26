import re

COMMON_PASSWORDS={
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "admin012345",
    "abcdefgh",
    "1234",
    "123456789",
    "password12345"
}

def check_password(password):
    score=0
    suggestions=[]

    if password.lower() in COMMON_PASSWORDS:
        return{
            "strength":"VERY WEAK",
            "score":0,
            "suggestions":["Avpoid Commonly used PAsswords"]
        }

    if len(password)>=8:
        score+=1
    else:
        suggestions.append(
            "Used at least 8 characters"
        )

    if len(password)>=12:
        score+=1
    else:
        suggestions.append(
            "Use 12 or more characters for better security"
        )

    if re.search(r"[A-Z]",password):
        score+=1
    else:
        suggestions.append(
            "Add a lower case letter"
        )

    if re.search(r"\d",password):
        score+=1
    else:
        suggestions.append(
            "Add a number"
        )

    if re.search(r"[^A-Za-z0-9]",password):
        score+=1
    else:
        suggestions.append(
            "Add a special character"
        )

    if score <=2:
        strength="weak"
    elif score <=4:
        strength="Medium"
    elif score ==5:
        strength="Strong"
    else:
        strength="veryStrong"

    return {
        "strength":strength,
        "score":score,
        "suggestions":suggestions
    }