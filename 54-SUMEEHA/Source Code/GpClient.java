
class  GpClient
  {              
//-----------------------------------------------------------------------
   public  static void main(String argv[]) throws Exception
     {     	
       GpSubs Sbrs = new GpSubs();

      try
        {   
           Sbrs.Design();                           
       } 
      catch(Exception e)
        {
         System.out.println(e.toString()+"Error ");               
      }
   }
}





