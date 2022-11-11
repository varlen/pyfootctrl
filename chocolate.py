def bank_letter(cc_index):
    return chr(65 + (cc_index % 4))

def bank_number(cc_index):
    return chr(49 + cc_index // 4)

def display(cc_index):
    return f'{bank_number(cc_index)}{bank_letter(cc_index)}'.upper()