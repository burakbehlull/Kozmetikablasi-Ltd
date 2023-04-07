<script lang="ts">
	import {Route, Router} from 'svelte-navigator'
	import Home from "./Home.svelte";
</script>

<Router>
	<Route path="/">
		<Home />
	</Route>

	<Route path="*">
		<h1>404</h1>
	</Route>
</Router>