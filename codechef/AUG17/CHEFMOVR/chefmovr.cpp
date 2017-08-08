#include <iostream>
using namespace std;

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);

    int t, n, d;
    int *arr = new int[n];

    cin >> t;
    while(t--) {
        cin >> n >> d;

        for(int i=0; i<n; i++) {
            cin >> arr[i];
        }

        for(int i=1; i<=n; i++) {
            sum = 0;
            sub_n = 0;
            for(int j=i; j<=n; j=j+d) {
                sum += arr[j];
                sub_n += 1;
            }

            if(sum%sub_n == 0) {
            }
        }
    }

    return 0;
}
