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

		function compareStrings(a, b) {
  			// Assuming you want case-insensitive comparison
  			a = a.toLowerCase();
  			b = b.toLowerCase();

  			return (a < b) ? -1 : (a > b) ? 1 : 0;
		}

		data.sort(function(a, b) {
  		return compareStrings(a, b);	
			})
});

</script>

{#if mounted}

{#each Object.entries(data) as [title,link]}

<li><a href={link}>{title}</a></li>
	
{/each}

{/if}

