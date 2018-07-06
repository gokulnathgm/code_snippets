#include<stdio.h>
void main(){
	int large, a[100000], t, n, index=0, contig=0, noncontig=0, i, j, k, total=0, p;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		scanf("%d",&n);
		for(j=0;j<n;j++){
			scanf("%d",&a[j]);
			if(j==0)
				large = a[0];
			if(a[j]>large)
				index = j;
		}
		noncontig = a[index];
		contig = a[index];

		for(k=0;k<n;k++){
			if(a[k]>0 && k!=index)
				noncontig+=a[k];
		}

		for(k=0;k<n-1;k++){
			total = a[k];
			for(p=k+1;p<n;p++){
				total+=a[p];
				if(total>contig)
					contig = total;
			}
		}
		printf("%d %d",contig,noncontig);	
	}
}