using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Gate202 : MonoBehaviour
{
    public Canvas fade;

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            fade.enabled = true;
        }
    }
}
