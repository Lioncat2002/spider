<script>
import {onMount} from 'svelte'
let mounted=false
let data={}
onMount(async () => {
        const response = await fetch('https://raw.githubusercontent.com/Lioncat2002/spider/main/web%20scraping/links.json');
        const res = await response.json();
        
		data=res
		mounted=true

		
});

</script>
<h2>
	Games:
</h2>
{#if mounted}
<ol>
	{#each Object.entries(data) as [title,link]}

	<li> <h3><a href={link}>{title}</a></h3> </li>
		
	{/each}
</ol>


{/if}

