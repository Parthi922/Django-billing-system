from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class ProductsView(APIView):
        

       
       # def get(self, request):
                
                # all_products = Products.objects.all()

               #  products_data = []

                # for product in all_products:
                        
                  #      Single_product = {
                  #              "id" : product.id,
                  #              "product_name" :product.product_name,
                  #              "cost" : product.code,
                  #             "price" : product.price
                  #      }
                  #             products_data.append(Single_product)
  

               # return Response(products_data)
        


        
        def get(self, request):
                
                all_products = Products.objects.all()

                serialized_products = products_serializers2(all_products, many=True).data

                print(serialized_products)

                return Response(serialized_products)


        #def post(self, request):
                
               # new_product = Products(product_name = request.data["product_name"], code = request.data["code"],price = request.data["price"], category_reference_id = request.data["category_reference_id"])
                
                #new_product.save()
                
               # return Response("Data Saved")
      
        def post(self, request):
                
                new_product = products_serializers(data= request.data)

                if new_product.is_valid():
                        
                        new_product.save()
                
                return Response("Data Saved")


class ProductsViewById(APIView):

        #def get(self, request, id):


                #product = Products.objects.get(id = id)
                
                #Single_product = {
                #         "id" : product.id,
                #        "product_name" :product.product_name,
                #        "cost" : product.code,
                #        "price" : product.price
                # }
                        

                #return Response(Single_product)
        

        def get(self, request, id):


                product = Products.objects.get(id = id)
                
                single_product = products_serializers2(product).data
                
                return Response(single_product)
        
        def patch(self, request, id):

                product = Products.objects.filter(id = id)


                product.update(product_name = request.data["product_name"], code = request.data["code"],price = request.data["price"])

                return Response("updated")
        
        def delete(self, request, id):

              product = Products.objects.get(id = id)

              product.delete()

              return Response("Delete")  
        

class CategoryView (APIView):

        def get(self, request):

                 all_category = Category_serializer(category.objects.all(), many=True).data
                 
                 return Response(all_category) 

           
        def post(self,request):

                new_categoy = Category_serializer(data=request.data)
                
                if new_categoy.is_valid():
                        
                        new_categoy.save()
                        
                        return Response("Data saved")
                   
                else:  
                        return Response(new_categoy.errors) 


class CategoryViewById(APIView):

        def delete(self , request , id):

                Category = category.objects.get(id = id)

                Category.delete()

                return Response ("deleted")