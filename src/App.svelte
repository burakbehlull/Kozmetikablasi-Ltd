<script lang="ts">
  	import Header from "./components/Header.svelte";
  	import Nav from "./components/Nav.svelte";

	const fetchImage = (async () => {
		const response = await fetch("http://127.0.0.1:5000/data")
		console.log(response)
    return await response.json()
	})()
	
</script>

<div>
	<!-- {JSON.stringify(fetchImage)} -->
<!-- 
	{#await fetchImage}
	<p>...waiting</p>
{:then data}
	{data.firstName}
	{data.lastName} 
	{data.Age} 
{:catch error}
	<p>An error occurred!</p>
{/await} -->

	<header>
		<Nav />
	</header>
	
	<main>	
		<Header />
	</main>

</div>

<style lang="scss">
	

</style>