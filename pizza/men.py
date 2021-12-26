import matplotlib.pyplot as plt

labels = "carlos", "vida", "gay"
sizes = [40,30,15,20]

figl, axl = plt.subplot()
axl.pie(sizes, labels=labels, autopct="%1.1f%%",
        shadow=True, startangle=90)
axl.axis("equal")
plt.show()