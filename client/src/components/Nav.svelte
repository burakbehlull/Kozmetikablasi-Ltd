<script lang="ts">
	let data;
	const getSettings = async()=> {
		const response = await fetch('http://127.0.0.1:5000/api/settings')
		const jsonData = await response.json()
		data = jsonData
		console.log(jsonData)
	}
	getSettings()
</script>

<nav>
    <ul>
        <li class="page-title"><a href="/">
        {#if data}
        {data[0].title}
        {:else}
        Kozmetik Abla
        {/if}
        </a></li>

        <li><a href="/home">Home</a></li>
        <li><a href="/home">Works</a></li>
        <li><a href="/home">Contact</a></li>
        <li><a href="/about">About</a></li>
    </ul>
</nav>

<style lang="scss">
    nav{
        
        ul{
           height: calc(8vh);
           padding-right: 20px;
           display: flex;
           list-style-type: none;
           gap: 15px;
           justify-content: flex-end;

           .page-title{
				margin-right: auto;
                padding-left: 20px;
				
			}
           li{
           
                a{
                    font-size: 1.1em;
                    font-weight: 500;
                    text-decoration: none;
                    color: #303030;
                }

            }
       }
    }
</style>