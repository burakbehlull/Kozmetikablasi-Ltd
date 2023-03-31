<script lang="ts">


</script>

<section>
    <div class="box-one">
        <div>BOX ONE</div>
        <div>BOX TWO</div>
        <div>BOX THREE</div>
    </div>
    <div class="box-two">
        <div>BOX FOUR</div>
        <div>BOX FIVE</div>
        <div>BOX SIX</div>
    </div>
</section>

<style lang="scss">
    section{
        height: calc(100vh);
        display: grid;
        row-gap: 10px;
        div{
            border-radius: 30px;
        }
        .box-one{
            display: grid;
            grid-template-areas:
            'ONE ONE TWO THREE';
            grid-template-columns: repeat(auto-fit, minmax(100px, 4fr));
            
            gap: 10px;
            div{
                padding: 130px;
                box-shadow: rgba(149, 157, 155, 0.2) 8px 8px 24px;
                
            }
            div:nth-child(1){
               
                grid-area: ONE;
                background-color: aqua;
            }
            div:nth-child(2){
            
                grid-area: TWO;
                background-color: blue;
            }
            
            div:nth-child(3){
                grid-area: THREE;
                background-color: red;
            }
        }
        .box-two{
            display: grid;
            grid-template-areas:
            'FOUR FIVE SIX';
            // grid-template-columns: repeat(3, 1fr,);
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
            gap: 10px;

            div{
                padding: 20px;
                box-shadow: rgba(149, 157, 155, 0.2) 8px 8px 24px;
            }

            div:nth-child(1){
                grid-area: FOUR;
                background-color: aqua;
            }
            div:nth-child(2){
                grid-area: FIVE;
                background-color: blue;
            }
            
            div:nth-child(3){
                grid-area: SIX;
                background-color: red;
            }
        }
    }

   

</style>