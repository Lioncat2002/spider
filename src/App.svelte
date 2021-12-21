<script>
import {onMount} from 'svelte'
let mounted=false
let data={}
onMount(async () => {
        const response = await fetch('https://raw.githubusercontent.com/Lioncat2002/spider/main/web%20scraping/links.json');
        const res = await response.json();
		console.log(res)
        
		data=res
		console.log(data)
		mounted=true

		
});

</script>

{#if mounted}
<ol>
	{#each Object.entries(data) as [title,link]}

	<li><a href={link}>{title}</a></li>
		
	{/each}
</ol>


{/if}

