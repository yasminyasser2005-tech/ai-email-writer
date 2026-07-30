from email_writer import generate_reply

print("AI Email Writer (paste a complaint, type 'exit' to quit)")
while True:
    complaint = input("\nCustomer complaint: ")
    if complaint.lower() == "exit":
        break
    print("\n--- Generated Reply ---\n")
    print(generate_reply(complaint))