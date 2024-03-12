from besser.BUML.notations.ocl.FactoryInstance import Factory
class Root_Handler:
    def __init__(self):
        self.root = None
        self.factory = Factory()
        self.all =[]

    def get_root(self):
        return self.root
    def pop(self):
        self.last_coll_exp = self.all.pop()
        self.add_to_root(self.last_coll_exp)
    def checkNumberOrVariable(self, txt):
        if txt.isnumeric():
            if "." in txt:
                return "real"
            else:
                return "int"
        else:
            return "var"

    def add_to_root(self,op):
        if len(self.all)==0:
            if self.root is None:
                self.root = op
            else:
                op.arguments.append(self.root)
                self.root = op
        else:
            self.all[-1].add_body(op)
    def pop_root(self,root):

        if self.root == self.last_coll_exp:
            self.root = None
            return self.last_coll_exp
        if hasattr(root, "arguments"):
            if self.last_coll_exp in root.arguments:
                root.arguments.remove(self.last_coll_exp)
                return self.last_coll_exp
            for args in root.arguments:
                self.pop_root(args)

    def print(self):
        self.handlePrint(self.root)
    def handle_ID(self,id):
        varID =self.factory.create_variable_expression(id,None)
        self.add_to_root(varID)
        # print('\x1b[6;30;42m' + 'handled ID, verify me!!!' + '\x1b[0m')
        pass


    def handle_bag(self, bag, operator):
        collectionLiteral = self.factory.create_collection_literal_expression("bag")
        infixOperator = None
        if operator is not None:
            infixOperator = self.factory.create_infix_operator(operator)
        for item in bag:
            collectionLiteral.add_to_collection_items(self.factory.create_collection_item("bag",item))
        if infixOperator is not None:
            left = self.pop_root(self.root)

            operationCallExp = self.factory.create_operation_call_expression(left,collectionLiteral,infixOperator)

            self.add_to_root(operationCallExp)

    def handlePrimaryExp(self,primaryExp,operator):
        pass


    def handle_collection(self,oclExp):

        collectionOperator = None
        if "forAll" in oclExp[0:8]:
            collectionOperator = "forAll"
            pass
        elif "exists" in oclExp[0:8]:
            collectionOperator = "exists"
            pass
        elif "collect" in oclExp[0:9]:
            collectionOperator = "collect"
            pass
        elif "select" in oclExp[0:8]:
            collectionOperator = "select"
            pass

        print("Collection Operator: " + collectionOperator)
        self.handleColl(oclExp,collectionOperator)

        pass

    def handleColl(self, forAllExp,collectionOperator):

        self.all.append(self.factory.create_loop_expression(collectionOperator))
        without_arrow = forAllExp.replace("->", '')
        without_collOp = without_arrow.replace(collectionOperator+"(", '')
        if "|" in without_collOp:
            iterator = without_collOp.split("|")[0]
            multiple_variable = iterator.split(',')
            for variable in multiple_variable:
                iteratorParts = variable.split(':')
                iteratorVariableName = iteratorParts[0]
                if ":" in variable:
                    iteratorclass = iteratorParts[1]
                else:
                    iteratorclass = "NotMentioned"
                iteratorExp = self.factory.create_iterator_expression(iteratorVariableName ,iteratorclass)
                self.all[-1].addIterator(iteratorExp)

        pass
    def handle_binary_expression(self, expression, operator,inbetween= None):
        expressionParts = expression.split(operator)

        leftside = self.checkNumberOrVariable(expressionParts[0])
        rightside = self.checkNumberOrVariable(expressionParts[1])

        leftPart = None
        rightPart = None

        if "var" in leftside:
            leftPart = self.factory.create_variable_expression(expressionParts[0], type="NP")
        elif "int" in leftside:
            leftPart = self.factory.create_integer_literal_expression("NP", int(expressionParts[0]))
        elif "real" in leftside:
            leftPart = self.factory.create_real_literal_expression("NP", float(expressionParts[0]))

        if "var" in rightside:
            rightPart = self.factory.create_variable_expression(expressionParts[1], type="NP")
        elif "int" in rightside:
            rightPart = self.factory.create_integer_literal_expression("NP", int(expressionParts[1]))
        elif "real" in rightside:
            rightPart = self.factory.create_real_literal_expression("NP", float(expressionParts[1]))

        infixOperator = self.factory.create_infix_operator(operator)
        inBetweenOp = None
        if inbetween is not None:
            inBetweenOp = self.factory.create_infix_operator(inbetween)


        opeartion_call_exp = self.factory.create_operation_call_expression(leftPart, rightPart, infixOperator,
                                                                           inBetweenOp)
        self.add_to_root(opeartion_call_exp)


        pass

    def handlePrint(self, root):

        print(root)

        if hasattr(root, 'arguments'):
            if len(root.arguments) != 0:
                for arg in root.arguments:
                    self.handlePrint(arg)

