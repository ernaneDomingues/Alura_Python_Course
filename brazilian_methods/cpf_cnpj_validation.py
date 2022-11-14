from validate_docbr import CPF, CNPJ

class Document:
    @staticmethod
    def create_document(doc):
        if len(doc) == 11:
            return DocCpf(doc)
        elif len(doc) == 14:
            return DocCnpj(doc)
        else:
            raise ValueError('Invalid document!')

class DocCpf:
    def __init__(self, doc):
        if self.cpf_validation(doc):
            self.cpf = doc
        else:
            raise ValueError('Invalid CPF!')

    def __str__(self):
        return self.cpf_format()

    def cpf_validation(self, doc):
        validate = CPF()
        return validate.validate(doc)

    def cpf_format(self):
        mask = CPF()
        return mask.mask(self.cpf)

class DocCnpj:
    def __init__(self, doc):
        if self.cnpj_validation(doc):
            self.cnpj = doc
        else:
            raise ValueError('Invalid CNPJ!')

    def __str__(self):
        return self.cnpj_format()

    def cnpj_format(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)

    def cnpj_validation(self, doc):
        validate = CNPJ()
        return validate.validate(doc)

# class CpfCnpj:
#     def __init__(self, doc, type_doc):
#         self.type_doc = type_doc
#         doc = str(doc)
#         if self.type_doc == 'cpf':
#             if self.cpf_validation(doc):
#                 self.cpf = doc
#             else:
#                 raise ValueError('Invalid CPF!')
#         elif self.type_doc == 'cnpj':
#             if self.cnpj_validation(doc):
#                 self.cnpj = doc
#             else:
#                 raise ValueError('Invalid CNPJ!')
#         else:
#             raise ValueError('Invalid document!')
#
#     def __str__(self):
#         if self.type_doc == 'cpf':
#             return self.cpf_format()
#         elif self.type_doc == 'cnpj':
#             return self.cnpj_format()
#
#
#     def cpf_validation(self, cpf):
#         if len(cpf) == 11:
#             validate = CPF()
#             return validate.validate(cpf)
#         else:
#             raise ValueError('Number of invalid digits!')
#
#     def cpf_format(self):
#         mask = CPF()
#         return mask.mask(self.cpf)
#
#     def cnpj_validation(self, cnpj):
#         if len(cnpj) == 14:
#             validate = CNPJ()
#             return validate.validate(cnpj)
#         else:
#             raise ValueError('Number of invalid digits!')
#
#     def cnpj_format(self):
#         mask = CNPJ()
#         return mask.mask(self.cnpj)