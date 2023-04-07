<script lang="ts">
</script>

<section>
    <div class="box-one">
        <img src="./assets/note_ruj.avif" alt="Flormar Eyeliner" />
        <img src="./assets/flormar_eyeliner.jpg" alt="Flormar Eyeliner" />
        <img src="./assets/flormar_ruj.jpg" alt="Flormar Ruj" />
    </div>

    <div class="box-two">
        <img src="./assets/kozmetik_1.jpg" alt="kozmetik resimleri 1">
        <img src="./assets/kozmetik_2.jpg" alt="kozmetik resimleri 2">
        <img src="./assets/kozmetik_3.jpg" alt="kozmetik resimleri 3">
    </div>
</section>

<style lang="scss">
    section{
        height: calc(145vh);
        display: grid;
        .box-one{
            display: grid;
            grid-template-areas:
            'ONE ONE TWO THREE';
            grid-template-columns: repeat(auto-fit, minmax(10px, 4fr));

            gap: 10px;
            
            %imgTemplate{
                height: 90%;
                width: 100%;
                border-radius: 30px;
                box-shadow: rgba(149, 157, 155, 0.2) 8px 8px 24px;
                &:hover{
                    filter: brightness(0.95);
                    cursor: pointer;
                }
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

            
            %imgTemplate2{
                height: 90%;
                width: 100%;
                border-radius: 30px;
                box-shadow: rgba(149, 157, 155, 0.2) 8px 8px 24px;
                &:hover{
                    filter: brightness(0.95);
                    cursor: pointer;
                }
            }

            img:nth-child(1){
                @extend %imgTemplate2;
                grid-area: FOUR;
            }
            img:nth-child(2){
                @extend %imgTemplate2;
                grid-area: FIVE;
                background-color: blue;
            }
            
            img:nth-child(3){
                @extend %imgTemplate2;
                grid-area: SIX;
            }
        }
    }
</style>