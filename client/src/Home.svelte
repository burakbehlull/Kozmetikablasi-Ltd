<script lang="ts">
	import { onMount } from 'svelte'
  	import Header from "./components/Header.svelte";
  	import Nav from "./components/Nav.svelte";


	onMount(()=>{
		document.title = "Kozmetik Abla"
	})
</script>

<div>
	<header>
		<Nav />
	</header>
	
	<main>	
		<Header />
	</main>
</div>

<style lang="scss">
	

</style>