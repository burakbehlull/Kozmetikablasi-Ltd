<script lang="ts">
</script>

<section>
    <div class="box-one">
        
        <img src="./assets/note_ruj.avif" alt="Flormar Eyeliner" />
        <img src="./assets/flormar_eyeliner.jpg" alt="Flormar Eyeliner" />
        <img src="./assets/flormar_ruj.jpg" alt="Flormar Ruj" />
        
        
    </div>
    <div class="box-two">
        <div>BOX FOUR</div>
        <div>BOX FIVE</div>
        <div>BOX SIX</div>
    </div>
</section>

<style lang="scss">
    section{
        height: calc(145vh);
        display: grid;
        // row-gap: 10px;
        .box-one{
            display: grid;
            grid-template-areas:
            'ONE ONE TWO THREE';
            grid-template-columns: repeat(auto-fit, minmax(100px, 4fr));

            gap: 10px;
            
            %imgTemplate{
                border-radius: 30px;
                box-shadow: rgba(149, 157, 155, 0.2) 8px 8px 24px;
                height: 95%;
                width: 100%;
            }
            img:nth-child(1){
                @extend %imgTemplate;
                grid-area: ONE;
            }
            img:nth-child(2){
                @extend %imgTemplate;
                grid-area: TWO;
            }
            
            img:nth-child(3){
                
                @extend %imgTemplate;
                grid-area: THREE;
                
            }
        }
        .box-two{
            display: grid;
            grid-template-areas:
            'FOUR FIVE SIX';
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