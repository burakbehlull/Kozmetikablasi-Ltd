<script lang="ts">
  	import Nav from "./components/Nav.svelte";
	
	export let firstName: string;
</script>

<div>
	<header>
		<Nav />
	</header>

	<main></main>

</div>

<style lang="scss">
	*{
		margin: 0;
		padding: 0;
	}
</style>